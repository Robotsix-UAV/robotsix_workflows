#!/bin/bash
set -e

# Setup ROS2 environment
source "/opt/ros/$ROS_DISTRO/setup.bash"
source "/ros_ws/install/setup.bash"

# Start a tmux session named 'uav_session'
tmux new-session -s uav_session
