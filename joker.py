

from os import *
from sys import *
from time import *
###		    colors
R='\033[1;31m'
G='\033[1;32m'
Y='\033[1;33m'
C='\033[1;36m'
W='\033[1;37m'

#12###	            banner
system('termux-open https://www.youtube.com/channel/UCVdrCnqGny9vbeim_p18b3Q')
system('clear')
system('toilet -f mono12 -F gay joker')
print("\033[1;32m       ShadoW--{ ^_^ }--Welcome To Tool Joker ")
print("\033[1;37m       ====================================== ")
print(" ")
print ( G +"["+ R +"1" + G +"]"+ W +"=="+ G +"["+ Y +"Install Metasploit"+ G +"]")
system('sleep 0.1')
print ( G +"["+ R +"2" + G +"]"+ W +"=="+ G +"["+ Y +"Install App Port  "+ G +"]")
system('sleep 0.1')
print ( G +"["+ R +"3" + G +"]"+ W +"=="+ G +"["+ Y +"Check Port Open   "+ G +"]")
system('sleep 0.1')
print ( G +"["+ R +"4" + G +"]"+ W +"=="+ G +"["+ Y +"Check Port Nmap   "+ G +"]")
system('sleep 0.1')
print ( G +"["+ R +"5" + G +"]"+ W +"=="+ G +"["+ Y +"Payload Android   "+ G +"]")
system('sleep 0.1')
print ( G +"["+ R +"6" + G +"]"+ W +"=="+ G +"["+ Y +"Payload Windows   "+ G +"]")
system('sleep 0.1')
print ( G +"["+ R +"7" + G +"]"+ W +"=="+ G +"["+ Y +"Exploit Android   "+ G +"]")
system('sleep 0.1')
print ( G +"["+ R +"8" + G +"]"+ W +"=="+ G +"["+ Y +"Exploit Windows   "+ G +"]")
system('sleep 0.1')
print ( G +"["+ R +"9" + G +"]"+ W +"=="+ G +"["+ Y +"Upload Payload    "+ G +"]")
system('sleep 0.1')
print ( G +"["+ R +"10" + G +"]"+ W +"=="+ G +"["+ Y +"Password Android "+ G +"]")
system('sleep 0.1')
print ( G +"["+ R +"11" + G +"]"+ W +"=="+ G +"["+ Y +"About "+ G +"           ]")
system('sleep 0.1')
print ( G +"["+ R +"0" + G +"]"+ W +"=="+ G +"["+ Y +"Exit program      "+ G +"]")

print(" ")

droid=str(input(R +"              ●~"+ G +"Enter Number "+ R +"~》 "+ G))

if droid == "1":
    system('clear')
    print (Y +"    {+\+\+\+ Install Now MetaSploit +/+/+/+}")
    system('sleep 1')
    system('pkg install unstable-repo -y')
    system('pkg install metasploit -y')
    system('clear')
    print (G +"            ^_^ ...... Thank You Down")
    print (C +"Please Open New Session and Enter") 
    print (C +"                         The command---"+ Y +"{ "+ W +"msfconsole "+ Y +"}")
    print (" ")
    print (R +"*"*54)
    print (" ")
    print (" ")
    input (G +"Enter BaCk... ")
    system('python joker.py')
elif droid == "2":
    system('clear')
    print (G +"Downloading ...... ")
    system('termux-open https://download844.mediafire.com/839hbkedq6kg/hqqdm6u76ol4mve/Port+Forwarder_v6.1_apkpure.com.apk')
    system('clear')
    print ("Please Go /sdcard/Download "+ Y +"Install App")
    print (R +"*"*54)

    input(G +"Enter BaCk... ")
    system('python joker.py')

elif droid=="3":
    print("         please Go URL")
    sleep(2)
    system('termux-open https://canyouseeme.org/')
    system('')
    print(R +"*"*54)
    print(" ")
    print(" ")
    input(G +"Enter BaCk... ")
    system('python joker.py')
elif droid=="4":
    system('clear')
    system('bash .nmap.sh')
elif droid=="5":
    system('clear')
    system('bash .paya.sh')
elif droid=="6":
    system('clear')
    system('bash .payw.sh')
elif droid=="7":
    system('clear')
    system('bash .msf.sh')
elif droid=="8":
    system('clear')
    system('bash .msfw.sh')
elif droid=="9":
    system('clear')
    system('termux-open  https://www.up-4.net/?op=upload')
    system('python3 joker.py')
elif droid=="11":
    system('clear')
    system('bash .about.sh')
elif droid=="10":
    system('clear')
    system('mkdir JOKER-EGYPT')
    system('cp -a .pass.apk /sdcard/JOKER-EGYPT/pass.apk')
    system('clear')
    print(" ")
    print(" ")
    print(" ")
    print(R +"           Password Is=~:"+ G +"   422002")
    exit()
elif droid=="0":
    system('clear')
    print(Y +"Good Bay Frind Please No forget subscribe my channel ^_•")
    print(R +"*"*52)
    exit()
else:
	system('clear')
	print(R +"Error  "*100)
	print(Y +"Please Enter Number Successful ^_^")
	sleep(1)
	system('python joker.py')
