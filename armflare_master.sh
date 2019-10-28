#!/bin/bash

#Usage: source rossetup.sh
#Sets up ROS variables to communicate with the ros master running on realtime.local (the kuka computer)

export ROS_MASTER_URI=http://armflare.local:11311
export ROS_HOSTNAME=$(ifconfig enp5s0 | grep "inet addr" | awk -F: '{print $2}' | awk '{print $1}')

# echo 'This must be sourced, not run'
