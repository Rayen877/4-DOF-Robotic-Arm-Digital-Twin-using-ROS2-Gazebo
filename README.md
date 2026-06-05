# 4-DOF-Robotic-Arm-Digital-Twin-using-ROS2-Gazebo
Overview
This project presents a digital twin system for a 4-DoF robotic arm, connecting a simulated robot in Gazebo with a real hardware implementation.

The objective is to replicate the same movements from simulation onto the physical robotic arm in real time.

System Architecture
ROS 2 handles communication between all system components
Gazebo simulates the robotic arm and environment
MoveIt 2 performs motion planning and trajectory generation
ROS 2 Control manages joint-level control in simulation
ESP32 executes commands on the physical robotic arm
Custom servo driver board ensures safe actuation using optocoupler isolation
