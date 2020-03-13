import os
import signal
import getpass
import subprocess

#ExitCode
def exitcode(x, y):
	print("Thank You for Using!")
	exit()

signal.signal(2, exitcode)
#

def javacheck():
	ch1 = str(subprocess.getoutput("java -version"))
	if ("Java HotSpot" in ch1):
		print("Java Found!")
		hadoopcheck()
	
	else:
		print("Java Not Found! Please install Java first\nThe program will exit now...")
		exit()

def hadoopcheck():
	ch2 = str(subprocess.getoutput("hadoop version"))
	if ("hadoop/hadoop-core" in ch2):
		print("Hadoop Found!")
		sel = int(input("What do you want this node to be:\n1.Namenode\t2.Datanode\n"))
		if (sel == 1):
			print("Configuring Namenode...")
			nnconf()
		elif (sel == 2):
			print("Configuring Datanode...")
			dnconf()
		else:
			print("This is a wrong selection")
	else:
		print("Hadoop Not Found! Please install Hadoop first\nThe program will exit now...")
		exit()

def nnconf():
	os.system("mkdir /netdir")
	#hdfs-site.xml
	os.system("sed -i 's+</configuration>++g' /etc/hadoop/hdfs-site.xml)
	os.system("sed -i 's+<configuration>+<configuration>\\n\\n<property>\\n<name>dfs.name.dir</name>\\n<value>/master</value>\\n</property>\\n\\n</configuration>+g' /etc/hadoop/hdfs-site.xml")
	#core-site.xml
	mip = str(subprocess.getoutput("ifconfig enp0s3 | grep netmask | awk 'print{$2}'")
	os.system("sed -i 's+</configuration>++g' core-site.xml)
os.system("sed -i 's+<configuration>+<configuration>\\n\\n<property>\\n<name>fs.default.name</name>\\n<value>hdfs://"+mip+":9001"+"</value>\\n</property>\\n\\n</configuration>+g' /etc/hadoop/core-site.xml")
	#format master
	os.system("hadoop namenode format")
	os.system("iptables -F")
	os.system("hadoop-daemon.sh")
	scstat=str(subprocess.getoutput("jps"))
	if( "ame" in scstat ):
		print("Hadoop Setup Successful! To access user portal goto http://"+mip+":50070")
	else:
		print("Some error occured in starting the service")

def dnconf():
	#host-name
	os.system("hostnamectl set-hostname datanode.ts-client.com")	
	#hdfs-site.xml
	os.system("mkdir /data")
	os.system("sed -i 's+</configuration>++g' /etc/hadoop/hdfs-site.xml)
	os.system("sed -i 's+<configuration>+<configuration>\\n\\n<property>\\n<name>dfs.data.dir</name>\\n<value>/data</value>\\n</property>\\n\\n</configuration>+g' /etc/hadoop/hdfs-site.xml")
	#core-site.xml
	os.system("sed -i 's+</configuration>++g' /etc/hadoop/core-site.xml)
	os.system("sed -i 's+<configuration>+<configuration>\\n\\n<property>\\n<name>fs.default.name</name>\\n<value>hdfs://(mip):9001"+"</value>\\n</property>\\n\\n</configuration>+g' /etc/hadoop/core-site.xml")
	#format master
	os.system("hadoop namenode format")
	os.system("iptables -F")
	os.system("hadoop-daemon.sh")
	os.system("rm -f /tmp/jdk.rpm")
	os.system("rm -f /tmp/hadoop.rpm")

#Welcome Screen
os.system("tput setaf 4")
print("\tWelcome to Hadoop Setup Program")
os.system("tput setaf 0")
print("++++++++++++++++++++++++++++++++++++++++++++++")
#

#Security Protocol
passcode = "privilege"
temppass = getpass.getpass("Please enter the password: ")
if temppass !=  passcode:
	print("The password is incorrect!!!\nThe program will exit now.")
	exit()
#

#Program Body
print("Please wait while we check Java and Hadoop installations...\n")
javacheck()




