cmake_minimum_required(VERSION 3.0.2)
project(mqtt_bridge)

find_package(catkin REQUIRED COMPONENTS rospy std_msgs message_generation)
catkin_python_setup()
add_message_files(
  FILES
  computer_info.msg
)
generate_messages(DEPENDENCIES std_msgs)
catkin_package()




install(PROGRAMS
  scripts/mqtt_bridge_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

install(DIRECTORY config
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/config
)

add_custom_target(install_depends ALL COMMAND "pip3" "install" "--user" "-r" "${PROJECT_SOURCE_DIR}/requirements.txt")
