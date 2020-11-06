#!/bin/sh

echo "Total argument: $#"
echo "Script name: $0"
echo "Argument 1: $1"

#roslaunch gazebo_ros IMR_DF_NORMAL.launch
python3 rand_script_generation.py $1
echo *** generated camera XYZ ***
cat camera_script.txt
python camera_control/camera_scripting.py
