# Ogmen_robotics
Bot_description :
Has urdf file describing the robot structure with stl files imported from blender after resizing.
Has launch files to spawn the robot in gazebo,rviz_visualiztion and controlling the robot.

Command: ros2 launch bot_decription launch-file.launch.py
For Controlling the robot run teleop_twist_keyboard teleop_twist_keyboard in a new terminal.



Bot_world:

Has launch files to spawn the robot in gazebo with the given model.
Command: ros2 launch bot_world launch-file.launch.py


Bot_controller:

Has launch files to get the filtered scan data and visualize it in rviz.
Has a script subscribing the the laser_scan topic and then publishing the filtered data on /filtered_topic.
Command: ros2 launch bot_controller launch-file.launch.py


