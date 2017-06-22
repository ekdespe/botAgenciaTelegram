#!/bin/bash

fping -c1  -g 192.168.3.0/24 2>/dev/null >  alive.txt
>listaNomes.txt

while read line 
do  
	 fgrep `arp -a  $line | cut -d" " -f4` bancoDados | cut -d= -f1 >>listaNomes.txt
 
done < alive.txt
rm alive.txt
