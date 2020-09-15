# Description
This is a implementation of the TOPP-RA algorithm.

# Building Tests

```sh
# clone
git clone -b develop https://github.com/hungpham2511/toppra

# build
export LD_LIBRARY_PATH=/opt/openrobots/lib:${LD_LIBRARY_PATH}
export CMAKE_PREFIX_PATH=/opt/openrobots
mkdir build && cd build && cmake -DBUILD_WITH_PINOCCHIO=ON -DBUILD_WITH_qpOASES=ON ..
make -j4

# run test
./tests/all_tests
```

## Running test with pinocchio

Install pinocchio bindings and exmaple from robotpkg, then setup
environment variables:

``` sh
export ROS_PACKAGE_PATH=/opt/openrobots/share
export PYTHONPATH=/opt/openrobots/lib/python3.6/site-packages:$PYTHONPATH
# or any python version that you install
```


# Using TOPPRA in CMake-based project

In your CMakeLists.txt,
```cmake
# The following line defines cmake target toppra::toppra
find_package(toppra)
...
target_link_library(foo PUBLIC toppra::toppra)
```

## How to install optional dependencies:

- GLPK: `sudo apt install libglpk-dev`
- qpOASES: `sudo apt install robotpkg-qpoases` (follow http://robotpkg.openrobots.org/debian.html for robotpkg)
- pinocchio: `sudo apt install robotpkg-pinocchio` (follow http://robotpkg.openrobots.org/debian.html for robotpkg)


# Building bindings

- Install pybind11 2.5.0
- Build toppra-cpp with bindings on
``` sh
cmake -GNinja -DCMAKE_EXPORT_COMPILE_COMMANDS=1 -DBUILD_WITH_PINOCCHIO=ON -DBUILD_WITH_qpOASES=ON -DBUILD_WITH_GLPK=ON -DPYTHON_BINDINGS=ON -DPYBIND11_PYTHON_VERSION=3.7 ..
# change to 3.8 or other version as needed.
```
- Install toppra python normally.


