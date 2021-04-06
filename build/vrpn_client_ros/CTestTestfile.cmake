# CMake generated Testfile for 
# Source directory: /home/arijitnoobstar/Flapping-Wing-MAV/src/vrpn_client_ros
# Build directory: /home/arijitnoobstar/Flapping-Wing-MAV/build/vrpn_client_ros
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_vrpn_client_ros_roslint_package "/home/arijitnoobstar/Flapping-Wing-MAV/build/vrpn_client_ros/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/arijitnoobstar/Flapping-Wing-MAV/build/vrpn_client_ros/test_results/vrpn_client_ros/roslint-vrpn_client_ros.xml" "--working-dir" "/home/arijitnoobstar/Flapping-Wing-MAV/build/vrpn_client_ros" "--return-code" "/opt/ros/melodic/share/roslint/cmake/../../../lib/roslint/test_wrapper /home/arijitnoobstar/Flapping-Wing-MAV/build/vrpn_client_ros/test_results/vrpn_client_ros/roslint-vrpn_client_ros.xml make roslint_vrpn_client_ros")
add_test(_ctest_vrpn_client_ros_roslaunch-check_launch "/home/arijitnoobstar/Flapping-Wing-MAV/build/vrpn_client_ros/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/arijitnoobstar/Flapping-Wing-MAV/build/vrpn_client_ros/test_results/vrpn_client_ros/roslaunch-check_launch.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/arijitnoobstar/Flapping-Wing-MAV/build/vrpn_client_ros/test_results/vrpn_client_ros" "/opt/ros/melodic/share/roslaunch/cmake/../scripts/roslaunch-check -o \"/home/arijitnoobstar/Flapping-Wing-MAV/build/vrpn_client_ros/test_results/vrpn_client_ros/roslaunch-check_launch.xml\" \"/home/arijitnoobstar/Flapping-Wing-MAV/src/vrpn_client_ros/launch\" ")
subdirs("gtest")
