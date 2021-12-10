

1、python connect_mysql_det_ip.py 
运行该程序，实现摄像头ip的监测，读取当前路径下的“社区-摄像头对应表”的摄像头IP。
如果ping不通，则关闭**检测系统监测进程 + 发送邮件通知并将ping不通的摄像头IP一并发送。
**监测进程关闭后，**监测控制脚本监测到后会重新启动再次连接之前连不上的摄像头IP

2、ip_det.sh
该程序是不停的循环摄像头ip,每隔10分钟进行轮询ping摄像头IP，10分钟可以根据实际需求更改。（代码中为sleep 600）
并将运行结果追加保存在output.txt文件中。
设置了定时重启 每天1.30
重启后 前天日志备份到output_backup.txt文件中。
output.txt 文件置空，进行新一天运行结果的保存，起到定时清除日志的作用，防止内存溢出。

3、kill_ip_det.sh
该脚本实现kill ip_det脚本。即定时启动ip_det.sh ,定时kill_ip_det.sh 。




