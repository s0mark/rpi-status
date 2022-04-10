TOT=`cat /proc/meminfo | grep MemTotal: | awk '{print $2}'`
USED=`cat /proc/meminfo | grep Active: | awk '{print $2}'`
echo -n $USED $TOT
