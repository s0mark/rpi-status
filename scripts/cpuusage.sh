echo -n `top -bn2 -d 1 | grep 'Cpu(s)' | awk '{print $2+$4}' | tail -n1`
