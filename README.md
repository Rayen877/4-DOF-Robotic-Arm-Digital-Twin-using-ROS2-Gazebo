# 4-DOF-Robotic-Arm-Digital-Twin-using-ROS2-Gazebo
Overview
# Digital Twin of a 4-DoF Robotic Arm with ROS 2 and ESP32

---

## Overview

This project presents a **digital twin system** for a 4-DoF robotic arm, connecting a simulated robot in Gazebo with a real hardware implementation.

The objective is to replicate the same movements from simulation onto the physical robotic arm in real time.

---

## System Architecture

- **ROS 2** handles communication between all system components.
- **Gazebo** simulates the robotic arm and its environment.
- **MoveIt 2** performs motion planning and trajectory generation.
- **ROS 2 Control** manages joint-level control in simulation.
- **ESP32** receives commands from ROS 2 and controls the physical robotic arm.
- **Custom servo driver board** ensures safe actuation using optocoupler isolation.

---

## Key Features

- 4-DoF robotic arm simulation in Gazebo.
- Motion planning and trajectory execution using MoveIt 2.
- Joint control through ROS 2 Control.
- Communication between the digital twin and physical robot.
- ESP32-based servo motor control.
- Custom-designed servo control board with optocoupler isolation.
- Synchronization between the virtual and physical robotic arms.

---

## Technologies Used

- ROS 2
- Gazebo
- MoveIt 2
- ROS 2 Control
- ESP32
- Arduino Framework
- Servo Motors
- Optocouplers

---

## Applications

- Robotics research and education
- Industrial automation prototyping
- Digital twin development
- Remote monitoring and control
- Embedded systems integration

---

## Project Objective

The main goal of this project is to demonstrate how a digital twin can bridge the gap between simulation and reality by allowing a virtual robotic arm to accurately reproduce its movements on a physical robotic system.

This approach enables safer testing, faster development, and easier validation of robotic applications before deployment on real hardware.
