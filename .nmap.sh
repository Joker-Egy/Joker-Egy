
clear
##############   colors
c='\033[1;36m'
g='\033[1;32m'
r='\033[1;31m'
y='\033[1;33m'
b='\033[1;34m'
p='\033[1;35m'
w='\033[0m'
##############   Banner


echo -e "   $r"
echo -e "$blue"
echo "          [1]Check the ip "
echo "          [2]All Devices  "
echo "          [3]Guess on ip  "
echo -e "   "
echo -e "   "
echo -e "   $g"

read -p "         ●~Enter Number~: " nmap

checkip(){
ead -p "            ip-------->" ip
apt $n  nmap -y
clear
nmap $ip
sleep 3
read -p "                   ------------>entar"
python joker.py
}
############################################
checkall(){
apt $n  nmap -y
clear
nmap -sn 192.168.1.1/24
read -p "******************* >Entar   BaCk"
python joker.py
}
############################################
guess(){
clear
python2 .zz.py
read "                          Enter Back"
python joker.py
}
###########################################



if [ "$nmap" -eq "1"  ]; then
        checkip

elif [ "$nmap" -eq "2"  ]; then
        checkall

elif [ "$nmap" -eq "3"  ]; then
	guess

else clear
python joker.py
fi






