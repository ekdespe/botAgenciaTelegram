
#capturar com tempo
tshark -i wlan1 -a duration:60 -w saida 2>/dev/null 

#filtrar apenas MAC's
tshark -r saida -T fields -e wlan.sa > ki

#filtrar e organizar por saida únic sort -u > saida
cat ki | sort -u > listaMacs




