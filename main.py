import requests
import os
import time

def main():
	os.system("clear")
	print('''\033[1;31m
            ______              
       .d$$$******$$$$c.        
    .d$P"            "$$c      
   $$$$$.           .$$$*$.    
 .$$ 4$L*$$.     .$$Pd$  '$b   
 $F   *$. "$$e.e$$" 4$F   ^$b  
d$     $$   z$$$e   $$     '$. 
$P     `$L$$P` `"$$d$"      $$ 
$$     e$$F       4$$b.     $$ 
$b  .$$" $$      .$$ "4$b.  $$ 
$$e$P"    $b     d$`    "$$c$F 
'$P$$$$$$$$$$$$$$$$$$$$$$$$$$  
 "$c.      4$.  $$       .$$   
  ^$$.      $$ d$"      d$P    
    "$$c.   `$b$F    .d$P"     
      `4$$$c.$$$..e$$P"        
          `^^^^^^^`
''')
	time.sleep(1.5)
	os.system("clear")
	print('''\033[1;32m
 ██▓ ██▓███    ██████ ▓█████ ▄▄▄       ██▀███   ▄████▄   ██░ ██ 
▓██▒▓██░  ██▒▒██    ▒ ▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒
▒██▒▓██░ ██▓▒░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░
░██░▒██▄█▓▒ ▒  ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██ 
░██░▒██▒ ░  ░▒██████▒▒░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓
░▓  ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒
 ▒ ░░▒ ░     ░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░
 ▒ ░░░       ░  ░  ░     ░    ░   ▒     ░░   ░ ░         ░  ░░ ░
 ░                 ░     ░  ░     ░  ░   ░     ░ ░       ░  ░  ░
                                               ░               

\033[1;36m[\033[1;93m01\033[1;36m]\033[1;35m Consult IP
\033[1;36m[\033[1;93m02\033[1;36m]\033[1;35m What is my IP?
\033[1;36m[\033[1;93m03\033[1;36m]\033[1;35m Consult your own IP
\033[1;36m[\033[1;93m04\033[1;36m]\033[1;35m Credits
\033[1;36m[\033[1;93m05\033[1;36m]\033[1;35m Back
''')

	op = input("IpSearch \033[1;31m>\033[1;32m>\033[1;33m>\033[1;36m ")
	
	if op == '1' or op == '01':

		os.system("clear")
		ip = input("Enter the IP you want to query >>>\033[1;95m ")
		request = requests.get('http://ip-api.com/json/{}'.format(ip))
		address_data = request.json()

		if 'message' not in address_data:

			os.system("clear")
			print()
			print('\033[1;32m! \033[1;34mIP found \033[1;32m!')
			print()
			print('\033[1;36mStatus: {}'.format(address_data['status']))
			print('\033[1;36mCountry: {}'.format(address_data['country']))
			print('\033[1;36mCountry acronym: {}'.format(address_data['countryCode']))
			print('\033[1;36mState: {}'.format(address_data['regionName']))
			print('\033[1;36mState acronym: {}'.format(address_data['region']))
			print('\033[1;36mCity: {}'.format(address_data['city']))
			print('\033[1;36mZip: {}'.format(address_data['zip']))
			print('\033[1;36mLatitude: {}'.format(address_data['lat']))
			print('\033[1;36mLongitude: {}'.format(address_data['lon']))
			print('\033[1;36mTimezone: {}'.format(address_data['timezone']))
			print('\033[1;36mProvider: {}'.format(address_data['isp']))
			print('\033[1;36mOrganization: {}'.format(address_data['org']))
			print('\033[1;36mAS: {}'.format(address_data['as']))
			print('\033[1;36mIP: {}'.format(address_data['query']))
			print()
		else:
			os.system("clear")
			print("\n\033[1;31m! IP not found !\n")

		nv = input('\033[1;33mDo you want to return to the menu? \033[1;32my\033[1;33m/\033[1;31mn\033[1;33m:\033[1;36m ')

		if nv == 'y' or nv == 'Y':
			main()
		else:
			os.system("clear")
			print("\n\033[1;33mBye-bye\n")
			exit()

	elif op == '02' or op == '2':
		os.system("clear")
		request = requests.get('http://ip-api.com/json/?')
		address_data = request.json()
		if 'message' not in address_data:
			print('\n\033[1;36mYour IP is: {}\n'.format(address_data['query']))
		nv = input('\033[1;33mDo you want to return to the menu? \033[1;32my\033[1;33m/\033[1;31mn\033[1;33m:\033[1;36m ')

		if nv == 'y' or nv == 'Y':
			main()
		else:
			os.system("clear")
			print("\n\033[1;33mBye-bye\n")
			exit()
	elif op == '03' or op == '3':
		os.system("clear")
		request = requests.get('http://ip-api.com/json/?')
		address_data = request.json()
		if 'message' not in address_data:
			os.system("clear")
			print()
			print('\033[1;32m! \033[1;34mIP found \033[1;32m!')
			print()
			print('\033[1;36mStatus: {}'.format(address_data['status']))
			print('\033[1;36mCountry: {}'.format(address_data['country']))
			print('\033[1;36mCountry acronym: {}'.format(address_data['countryCode']))
			print('\033[1;36mState: {}'.format(address_data['regionName']))
			print('\033[1;36mState acronym: {}'.format(address_data['region']))
			print('\033[1;36mCity: {}'.format(address_data['city']))
			print('\033[1;36mZip: {}'.format(address_data['zip']))
			print('\033[1;36mLatitude: {}'.format(address_data['lat']))
			print('\033[1;36mLongitude: {}'.format(address_data['lon']))
			print('\033[1;36mTimezone: {}'.format(address_data['timezone']))
			print('\033[1;36mProvider: {}'.format(address_data['isp']))
			print('\033[1;36mOrganization: {}'.format(address_data['org']))
			print('\033[1;36mAS: {}'.format(address_data['as']))
			print('\033[1;36mIP: {}'.format(address_data['query']))
			print()
		else:
			os.system("clear")
			print("\n\033[1;31m! IP not found !\n")

		nv = input('\033[1;33mDo you want to return to the menu? \033[1;32my\033[1;33m/\033[1;31mn\033[1;33m:\033[1;36m ')

		if nv == 'y' or nv == 'Y':
			main()

		else:
			os.system("clear")
			print("\n\033[1;33mBye-bye\n")
			exit()
	elif op == '04' or op == '4':
		os.system("clear")
		print('''\033[1;31m
66 108 97 99 107  72 101 108 108  84 101 97 109 

\033[1;31mTeam:\033[1;32m Black Hell Team
\033[1;31mDeveloped by:\033[1;32m Near Shelby (Leader)
\033[1;31mAPI:\033[1;32m http://ip-api.com/json/?\033[0;0m
''')

		nv = input('\033[1;33mDo you want to return to the menu? \033[1;32my\033[1;33m/\033[1;31mn\033[1;33m:\033[1;36m ')

		if nv == 'y' or nv == 'Y':
			main()

		else:
			os.system("clear")
			print("\n\033[1;33mBye-bye\n")
			exit()

	elif op == '05' or op == '5':
		os.system("clear")
		print('''
 ____  _            _      _   _      _ _   _____                    
| __ )| | __ _  ___| | __ | | | | ___| | | |_   _|__  __ _ _ __ ___  
|  _ \| |/ _` |/ __| |/ / | |_| |/ _ \ | |   | |/ _ \/ _` | '_ ` _ \ 
| |_) | | (_| | (__|   <  |  _  |  __/ | |   | |  __/ (_| | | | | | |
|____/|_|\__,_|\___|_|\_\ |_| |_|\___|_|_|   |_|\___|\__,_|_| |_| |_|
                                                                     ''')
		exit()

	else:
		os.system("clear")
		exit()

main()
