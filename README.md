# autonomous-rover

Autonomous outdoor rover built on ROS2 Humble, Nav2, and YOLO running on a Jetson Orin Nano Super.

## Hardware
- NVIDIA Jetson Orin Nano Super (8GB)
- Orbbec Astra Pro depth camera
- RPLidar A1
- 4WD chassis + L298N motor driver

## Stack
- ROS2 Humble
- Nav2 (navigation)
- YOLO (object detection)
- Ubuntu 22.04 / JetPack 6.2

## Workspace Setup
```bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone https://github.com/mkirby42/autonomous-rover.git
cd ~/ros2_ws && colcon build
source install/setup.bash
```
