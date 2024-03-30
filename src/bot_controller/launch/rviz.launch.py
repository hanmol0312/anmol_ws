import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    package_share_dir=get_package_share_directory("bot_controller")
    node=os.path.join(package_share_dir,"scripts","laser_reading.py")
    return LaunchDescription([
        


        Node(
        package='joint_state_publisher_gui',
        executable=node,
        name="laser_reader",
        ),
        

        Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'),
        
    ])