# CMake generated Testfile for 
# Source directory: /home/jasper/flap_ws/src/vrpn_client_ros
# Build directory: /home/jasper/flap_ws/build/vrpn_client_ros
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_vrpn_client_ros_roslint_package "/home/jasper/flap_ws/build/vrpn_client_ros/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/jasper/flap_ws/build/vrpn_client_ros/test_results/vrpn_client_ros/roslint-vrpn_client_ros.xml" "--working-dir" "/home/jasper/flap_ws/build/vrpn_client_ros" "--return-code" "/opt/ros/melodic/share/roslint/cmake/../../../lib/roslint/test_wrapper /home/jasper/flap_ws/build/vrpn_client_ros/test_results/vrpn_client_ros/roslint-vrpn_client_ros.xml make roslint_vrpn_client_ros")
add_test(_ctest_vrpn_client_ros_roslaunch-check_launch "/home/jasper/flap_ws/build/vrpn_client_ros/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/jasper/flap_ws/build/vrpn_client_ros/test_results/vrpn_client_ros/roslaunch-check_launch.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/jasper/flap_ws/build/vrpn_client_ros/test_results/vrpn_client_ros" "/opt/ros/melodic/share/roslaunch/cmake/../scripts/roslaunch-check -o \"/home/jasper/flap_ws/build/vrpn_client_ros/test_results/vrpn_client_ros/roslaunch-check_launch.xml\" \"/home/jasper/flap_ws/src/vrpn_client_ros/launch\" ")
subdirs("gtest")
