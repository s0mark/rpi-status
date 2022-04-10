cpuTemp0=$(cat /sys/class/thermal/thermal_zone0/temp 2>/dev/null) || cpuTemp0=0
cpuTemp1=$(echo "scale = 1; $cpuTemp0/1000" | bc)
echo -n $cpuTemp1