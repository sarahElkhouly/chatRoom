import socket
import threading
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234
def register():
	username = input("Please enter your desired username :")
	password = input("Please enter your desired password :")
	file = open("accountfile.txt","a")
	file.write(username)
	file.write(" ")
	file.write(password)
	file.write("\n")
	file.close()
	if login():
		print("You are now logged in...")
	else:
		print("You aren't logged in!")

def login():
	username = input("Please enter your username:")
	login.targ=username
	password = input("Please enter your password:")  
	for line in open("accountfile.txt","r").readlines(): # Read the lines
		login_info = line.split() # Split on the space, and store the results in a list of two strings
		if username == login_info[0] and password == login_info[1]:
			print("Correct credentials!")
			return username
	print("Incorrect credentials.")
	sys.exit()
 
ch = input("for login enter 1 for register enter 0 :")
if ch=='0':
	register()
elif ch=='1':
	login()
username=login.targ
print(username)


ip = input('Enter the IP Address:')

s.connect((ip, port))
s.send(username.encode('ascii'))

clientRunning = True

def receiveMsg(sock):
	serverDown = False
	while clientRunning and (not serverDown):
		try:
			#buffer to recive1024byte
			msg = sock.recv(1024).decode('ascii')
			print(msg)
		except:
			print('Server is Down. You are now Disconnected. Press enter to exit...')
			serverDown = True

threading.Thread(target = receiveMsg, args = (s,)).start()
while clientRunning:
	tempMsg = input()
	msg = username + '>>' + tempMsg
	if '**quit' in msg:
		clientRunning = False
		s.send('**quit'.encode('ascii'))
	else:
		s.send(msg.encode('ascii'))