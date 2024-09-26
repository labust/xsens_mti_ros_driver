from launch import LaunchDescription
import launch
from launch.actions import DeclareLaunchArgument, RegisterEventHandler
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import numpy as np
import os


package_prefix = get_package_share_directory("xsens_mti_driver")
path_to_imu_params = os.path.join(package_prefix, 'config', 'three_imu_xsens_params.yaml')



pi = np.pi

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('debug', default_value='false'),
        DeclareLaunchArgument('port_name', default_value='/dev/arduino_driver'),
        Node(
            package = "tf2_ros",
            namespace = "imu_setup",
            executable = "static_transform_publisher",
            # arguments = ["0", "0", "0", str(241.5 * pi / 180), "0", "0", "map", "bts_pool_nw"]
            arguments = ["0", "0", "0", str(151.5 * pi / 180), "0", "0", "map", "bts_pool_ne"]
        ),
        Node(
            package = "tf2_ros",
            namespace = "imu_setup",
            executable = "static_transform_publisher",
            arguments = ["0", "0", "0", "0", "0", "0", "imu_setup/base_link", "imu_setup/imu_link_1"]
        ),
        Node(
            package = "tf2_ros",
            namespace = "imu_setup",
            executable = "static_transform_publisher",
            arguments = ["0.02", "-0.1", "0.04", "0", "0", str(pi/2), "imu_setup/base_link", "imu_setup/imu_link_2"]
        ),
        Node(
            package = "tf2_ros",
            namespace = "imu_setup",
            executable = "static_transform_publisher",
            arguments = ["-0.08", "-0.02", "0.04", str(-pi/2), "0", str(pi/2), "imu_setup/base_link", "imu_setup/imu_link_3"]
        ),
        Node(
            package='xsens_mti_driver',
            executable='xsens_mti_node',
            namespace='imu_setup',
            name='imu1',
            parameters=[path_to_imu_params],
            remappings=[
                ("imu/acceleration", "imu1/acceleration"),
                ("imu/angular_velocity", "imu1/angular_velocity"),
                ("imu/data", "imu1/data"),
                ("imu/dq", "imu1/dq"),
                ("imu/dv", "imu1/dv"),
                ("imu/mag", "imu1/mag"),
                ("imu/time_ref", "imu1/time_ref")
            ]
        ),
        Node(
            package='xsens_mti_driver',
            executable='xsens_mti_node',
            namespace='imu_setup',
            name='imu2',
            parameters=[path_to_imu_params],
            remappings=[
                ("imu/acceleration", "imu2/acceleration"),
                ("imu/angular_velocity", "imu2/angular_velocity"),
                ("imu/data", "imu2/data"),
                ("imu/dq", "imu2/dq"),
                ("imu/dv", "imu2/dv"),
                ("imu/mag", "imu2/mag"),
                ("imu/time_ref", "imu2/time_ref")
            ]
        ),
        Node(
            package='xsens_mti_driver',
            executable='xsens_mti_node',
            namespace='imu_setup',
            name='imu3',
            parameters=[path_to_imu_params],
            remappings=[
                ("imu/acceleration", "imu3/acceleration"),
                ("imu/angular_velocity", "imu3/angular_velocity"),
                ("imu/data", "imu3/data"),
                ("imu/dq", "imu3/dq"),
                ("imu/dv", "imu3/dv"),
                ("imu/mag", "imu3/mag"),
                ("imu/time_ref", "imu3/time_ref")
            ]
        )
    ])

if __name__ == "__main__":
    generate_launch_description()
