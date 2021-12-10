#!/bin/sh
name='ip_det.sh'
echo $name
#while true
#do
#pkill -f $name
#done
#ps aux|grep $name |grep -v grep|cut -c 9-15|xargs kill -9
ID=`ps -ef | grep $name | grep -v "$0" | grep -v "grep" | awk '{print $2}'`
echo $ID
echo '-----------'
for id in $ID
do 
kill -9 $id
echo 'killed $id'
done
