import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    package_share_dir=get_package_share_directory("bot_description")
    urdf=os.path.join(package_share_dir,"urdf","bot.urdf")
    return LaunchDescription([
        


        Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        arguments=[urdf]),
        

        Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'),
        
    ])