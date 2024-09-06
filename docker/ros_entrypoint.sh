#!/bin/bash
set -e

# Setup ROS2 environment
source "/opt/ros/$ROS_DISTRO/setup.bash"
source "/ros_ws/install/setup.bash"

# Start a tmux session named 'uav_session'
  tmux new-session -d -s uav_session

# Keep the container running
tail -f /dev/null
