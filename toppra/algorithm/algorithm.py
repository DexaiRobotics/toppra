"""Abstract types for parametrization algorithm.
"""
from typing import Dict, Any, List, Tuple
import numpy as np
import abc

from ..constants import TINY
from toppra.interpolator import SplineInterpolator, AbstractGeometricPath
from toppra.constraint import Constraint
import toppra.interpolator as interpolator

import logging

logger = logging.getLogger(__name__)


class ParameterizationData(dict):
    """Parametrization output."""
    pass


class ParameterizationAlgorithm(object):
    """The base class of parameterization algorithms.

    This class serves as the specifications for all derived algorithms.  There are multiple
    variants of parametrization algorithms. The reachability-based solvers are
    :class:`toppra.algorithm.TOPPRA` and :class:`toppra.algorithm.TOPPRAsd`. Further, users can
    also select different solvers for each algorithm as well.

    For details on how to *construct* a :class:`ParameterizationAlgorithm` instance, refer to the
    specific class. It should be noted that all derived algorithms must follow the specifications
    documented in this abstract class.

    """

    def __init__(self, constraint_list, path, gridpoints=None):
        self.constraints = constraint_list
        self.path = path  # Attr
        self._problem_data = {}
        # Handle gridpoints
        if gridpoints is None:
            gridpoints = interpolator.propose_gridpoints(path, max_err_threshold=1e-3)
            logger.info(
                "No gridpoint specified. Automatically choose a gridpoint. See `propose_gridpoints`."
            )

        if (
            path.path_interval[0] != gridpoints[0]
            or path.path_interval[1] != gridpoints[-1]
        ):
            raise ValueError("Invalid manually supplied gridpoints.")
        self.gridpoints = np.array(gridpoints)
        self._N = len(gridpoints) - 1  # Number of stages. Number of point is _N + 1
        for i in range(self._N):
            if gridpoints[i + 1] <= gridpoints[i]:
                logger.fatal("Input gridpoints are not monotonically increasing.")
                raise ValueError("Bad input gridpoints.")

    @property
    def constraints(self) -> List[Constraint]:
        """Constraints of interests."""
        return self._constraints

    @constraints.setter
    def constraints(self, value: List[Constraint]) -> None:
        # TODO: Validate constraints.
        self._constraints = value

    @property
    def problem_data(self) -> ParameterizationData:
        """Intermediate data obtained while solving the path parametrization.. """
        return self._problem_data

    @abc.abstractmethod
    def compute_parameterization(self, sd_start: float, sd_end: float):
        """Compute the path parameterization subject to starting and ending conditions.

        After this method terminates, the attribute :attr:`~problem_data` will contain algorithm
        output, as well as the result. This is the preferred way of retrieving problem output.


        Parameters
        ----------
        sd_start:
            Starting path velocity. Must be positive.
        sd_end:
            Goal path velocity. Must be positive.

        """
        raise NotImplementedError

    def compute_trajectory(self, sd_start: float = 0, sd_end: float = 0, return_data: bool =
                           False) -> Tuple[AbstractGeometricPath, AbstractGeometricPath]:
        """Compute the resulting joint trajectory and auxilliary trajectory.

        This is a convenient method if only the final output is wanted.

        Parameters
        ----------
        sd_start:
            Starting path velocity.
        sd_end:
            Goal path velocity.
        return_data:
            If true, return a dict containing the internal data.

        Returns
        -------
        :
            A 2-tuple. The first element is the time-parameterized joint position trajectory or
            None If unable to parameterize. The second element is the
            time-parameterized auxiliary variable trajectory. Is None if
            unable to parameterize

        """
        sdd_grid, sd_grid, v_grid, K = self.compute_parameterization(
            sd_start, sd_end, return_data=True
        )

        # fail condition: sd_grid is None, or there is nan in sd_grid
        if sd_grid is None or np.isnan(sd_grid).any():
            return None, None

        # Gridpoint time instances
        t_grid = np.zeros(self._N + 1)
        skip_ent = []
        for i in range(1, self._N + 1):
            sd_average = (sd_grid[i - 1] + sd_grid[i]) / 2
            delta_s = self.gridpoints[i] - self.gridpoints[i - 1]
            if sd_average > TINY:
                delta_t = delta_s / sd_average
            else:
                delta_t = 5  # If average speed is too slow.
            t_grid[i] = t_grid[i - 1] + delta_t
            if delta_t < TINY:  # if a time increment is too small, skip.
                skip_ent.append(i)
        t_grid = np.delete(t_grid, skip_ent)
        gridpoints = np.delete(self.gridpoints, skip_ent)
        q_grid = self.path(gridpoints)

        traj_spline = SplineInterpolator(
            t_grid,
            q_grid,
            (
                (1, self.path(0, 1) * sd_start),
                (1, self.path(self.path.duration, 1) * sd_end),
            ),
        )

        if v_grid.shape[1] == 0:
            v_spline = None
        else:
            v_grid_ = np.zeros((v_grid.shape[0] + 1, v_grid.shape[1]))
            v_grid_[:-1] = v_grid
            v_grid_[-1] = v_grid[-1]
            v_grid_ = np.delete(v_grid_, skip_ent, axis=0)
            v_spline = SplineInterpolator(t_grid, v_grid_)

        self._problem_data.update(
            {"sdd": sdd_grid, "sd": sd_grid, "v": v_grid, "K": K, "v_traj": v_spline}
        )
        if self.path.waypoints is not None:
            t_waypts = np.interp(self.path.waypoints[0], gridpoints, t_grid)
            self._problem_data.update({"t_waypts": t_waypts})

        return traj_spline
