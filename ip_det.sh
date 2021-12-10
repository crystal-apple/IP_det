#!/bin/bash

#sleep 10

project='/home/fsym123/ip_det/connect_mysql_det_ip.py'
cp /home/fsym123/ip_det/output.txt /home/fsym123/ip_det/output_backup.txt
echo "">/home/fsym123/ip_det/output.txt

while true
do



for Pro in $project
do
#echo $Pro

PythonPid=`ps -ef | grep $Pro | grep -v grep | wc -l`
#echo $PythonPid

if [ $PythonPid -eq 0 ];
        then 
        
        nohup python -u $Pro >>/home/fsym123/ip_det/output.txt 2>&1 &
        #echo $PythonPid
        
        CurrentPythonPid=`ps -ef | grep $Pro | grep -v grep | wc -l`
        #echo $CurrentPythonPid
        
        if [ $CurrentPythonPid -ne 0 ];
        then
        
        echo $CurrentPythonPid
        echo "正在运行"
        
        fi
fi


sleep 600
done
done


