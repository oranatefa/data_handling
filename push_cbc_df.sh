#!/bin/bash


/home/oran/Desktop/result_handler/copy_data.sh
read -r SN < '/home/oran/Pictures/DO_NOT_DELETE/SN.txt'
df_folder="/home/oran/Desktop/result_handler/sys_${SN}/Pictures/"
to_folder="/home/omri/Desktop/systems/sys_${SN}/"

echo "copying from: $df_folder" 
echo "to $to_folder"
scp -r ${df_folder} omri@192.168.90.73:${to_folder} &&exit
