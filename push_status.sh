#!/bin/bash

current_ip=$(ip route get 8.8.8.8 | sed -n '/src/{s/.*src *\([^ ]*\).*/\1/p;q}')
echo "$current_ip"

cd /home/oran/Documents/sandbox
git_head=$(git rev-parse --verify HEAD) 
branch=$(git branch | awk '/\*/ { print $2; }')

cd /home/oran/git/efa-revdx-v2-sw
iot_git_head=$(git rev-parse --verify HEAD) 
iot_branch=$(git branch | awk '/\*/ { print $2; }') 

read -r SN < '/home/oran/Pictures/DO_NOT_DELETE/SN.txt'

ssh omri@192.168.90.73 /home/omri/Desktop/systems/run_print.sh  'SN' $SN 'IP' $current_ip 'HEAD' $git_head 'BRANCH' $branch 'IOT_HEAD' $iot_git_head 'IOT_BRANCH' $iot_branch  &&exit

