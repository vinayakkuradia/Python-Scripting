import os
import subprocess
import signal

ip = 0

#ExitCode
def exitcode(x, y):
	print("\nThank You for Using!")
	exit()

signal.signal(2, exitcode)
#

def pingcheck():
	global ip
	ip = str(input("Enter the IP of Remote Host:  "))
	x = str(subprocess.getstatusoutput("ping -c 1 " + ip))
	if( x[1] == "0" ):
		print("Ping to IP: "+ ip + " was successful")
	else:
		print("Connection to the IP: " + ip + " failed.\nPlease enter another IP or try again: ")
		pingcheck()

def operations():
	print("""
Press 1: To check Date
Press 2: To check Calender
Press 3: To check UserName
Press 4: To create File
Press 5: To create a User
Press 6: To Exit
	""")

	s = int(input("Enter the choice: "))

	if s == 1:
		os.system("date")
	elif s == 2:
		os.system("cal")
	elif s == 3:
		os.system("whoami")
	elif s == 4:
		fname = input("Please enter File Name: ")
		os.system("touch " + fname)
		print("The file is created")
	elif s == 5:
		username = input("Please enter the Name for the account: ")
		usrexist = subprocess.getstatusoutput("id {}".format(username))
		if (usrexist[2] == 0):
			usrcreate = subprocess.getstatusoutput("useradd {}".format(username))
			if ( usrcreate[2] == 0 ):
				print("The user was created successfully!")
		elif (str(usrexist).find(username)):
			print("The username is already available. Please try again")
		else:
			print("Unknown Error Occured!!!")

	
	elif s == 6:
		os.system("exit")
		print("\nThank You for Using!")
	else:
		print("Wrong Selection")


os.system("tput setaf 4")
print("\t\tWelcome to my tools")
os.system("tput setaf 0")
print("\t----------------------------------")


opt = str(input("Where do you want to execute operations(L/R):\n1.Local\t2.Remote\n"))
if opt == "L" or opt == "1":
	operations()
elif opt == "R" or opt == "2":
	pingcheck()
	print("Please enter password of remote host when asked: ")
	os.system("ssh {}".format(ip))
	operations()
else:
	print("Wrong Selection! The Program will exit now!\n")
	exit()	


