import os
import subprocess


def custom()
	print("This program will install and configure HTTPD Web Server: ")
	x = str(subprocess.getstatusoutput("yum install httpd -y"))
	if x[1] == "0":
		print("HTTPD Web Server Installed/nPlease wait while we configure it...")
		subprocess.getoutput("echo 'This is a test page!' > /var/www/html/index.html")
		subprocess.getstatusoutput("systemctl stop firewalld")
		subprocess.getstatusoutput("systemctl disable firewalld")
		os.system("semanage port -at http_port_t -p tcp "+port)
		os.system("mkdir /var/www/"+folder)
		os.system("sed -i 's+Listen 80+Listen "+port+"+g' /etc/httpd/conf/httpd.conf")
		os.system("sed -i 's+DocumentRoot \"/var/www/html\"+DocumentRoot \"/var/www/"+folder+"\"+g' /etc/httpd/conf/httpd.conf")
		y = str(subprocess.getstatusoutput("systemctl restart httpd"))
		subprocess.getstatusoutput("systemctl enable httpd")
		if y[1] == "0":
			print("HTTPD Service is running on port "+port+"./n")
		else:
			print("There was some problem starting the service! Please try again")
	
	else:
		print("The software was not installed due to some error.")

def express()
	print("This program will install and configure HTTPD Web Server: ")
	x = str(subprocess.getstatusoutput("yum install httpd -y"))
	if x[1] == "0":
		print("HTTPD Web Server Installed/nPlease wait while we configure it...")
		subprocess.getoutput("echo 'This is a test page!' > /var/www/html/index.html")
		subprocess.getstatusoutput("systemctl stop firewalld")
		subprocess.getstatusoutput("systemctl disable firewalld")
		y = str(subprocess.getstatusoutput("systemctl restart httpd"))
		subprocess.getstatusoutput("systemctl enable httpd")
		if y[1] == "0":
			print("HTTPD Service is running on port 80./n")
		else:
			print("There was some problem starting the service! Please try again")
	
	else:
		print("The software was not installed due to some error.")
