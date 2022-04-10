gpuTemp0=$(/opt/vc/bin/vcgencmd measure_temp 2>/dev/null)
gpuTemp1=${gpuTemp0//temp=/}
echo -n ${gpuTemp1//\'C/}