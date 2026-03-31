# autonomous-rover

Autonomous outdoor rover built on ROS2 Humble, Nav2, and YOLO running on a Jetson Orin Nano Super.

## Hardware
- NVIDIA Jetson Orin Nano Super (8GB) — JetPack 6.2 / L4T 36.4.3
- Orbbec Astra Pro depth camera (RGB + depth + IR)
- RPLidar A1 (ordered)
- 4WD chassis + L298N motor driver (ordered)
- 12V 5200mAh Li-ion battery + 12V→5V step-down converter (ordered)

## Stack
- ROS2 Humble (Ubuntu 22.04)
- Nav2 (navigation — Week 3)
- YOLOv8n (object detection — running)
- Foxglove Studio (remote visualization)

## Progress

### Week 1 ✅ (Days 1-5 completed in 2 days)
- [x] Jetson flashed and booted (JetPack 6.2)
- [x] SSH access via Tailscale (Pi + Mac)
- [x] ROS2 Humble installed
- [x] GitHub repo scaffolded
- [x] Orbbec Astra Pro streaming — RGB, depth, IR, point cloud at 30fps
- [x] YOLOv8n detection node running on live camera feed
- [x] Foxglove Studio visualization from Mac

### Week 2 (upcoming — waiting on chassis hardware)
- [ ] Assemble 4WD chassis
- [ ] Wire L298N motor driver
- [ ] Diff-drive ROS2 node (/cmd_vel → motors)
- [ ] Mount camera + lidar on chassis
- [ ] Odometry publisher

## Workspace Setup
```bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone https://github.com/mkirby42/autonomous-rover.git
cd ~/ros2_ws && colcon build --symlink-install
source install/setup.bash
```

## Remote Visualization
```bash
# On Jetson
ros2 launch foxglove_bridge foxglove_bridge_launch.xml

# On Mac — open Foxglove Studio, connect to ws://100.101.91.45:8765
```
