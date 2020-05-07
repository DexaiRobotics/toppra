"""TOPP-RA implements multiple path-parametrization algorithms.


Abstract class
^^^^^^^^^^^^^^^^^^^
.. autoclass:: toppra.algorithm.algorithm.ParameterizationData
   :members:

.. autoclass:: toppra.algorithm.algorithm.ParameterizationAlgorithm
   :members:

TOPPRA (time-optimal)
^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: toppra.algorithm.TOPPRA
   :members: problem_data, compute_parameterization, compute_trajectory, compute_feasible_sets, compute_controllable_sets

TOPPRAsd (specific-duration)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: toppra.algorithm.TOPPRAsd
   :members: problem_data, set_desired_duration, compute_parameterization, compute_trajectory, compute_feasible_sets, compute_controllable_sets


"""
from .algorithm import ParameterizationAlgorithm, ParameterizationData
from .reachabilitybased import TOPPRA, TOPPRAsd

__all__ = ["ParameterizationData", "ParameterizationAlgorithm", "TOPPRA", "TOPPRAsd"]
