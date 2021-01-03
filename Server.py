import socket
import threading

#socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverRunning = True
#hold ip address of the machine server is runing on it 
ip = str(socket.gethostbyname(socket.gethostname()))
#port num will be used 
port = 1234

clients = {}
#bind server to ip add and port 
s.bind((ip, port))
#server listen request 
s.listen()
#server status 
print('Server Ready...')
print('Ip Address of the Server::%s'%ip)

def handleClient(client, uname):
    clientConnected = True
    keys = clients.keys()
    help = 'There are four commands in our chat room\n1::**chatlist=>gives you the list of the people currently online\n2::**all=>To broadcast your message to each and every person currently present online\n3::Add the name of the person at the end of your message preceded by ** to send it to particular person\n4::**quit=>To end your session'

    while clientConnected:
        try:
            msg = client.recv(1024).decode('ascii')
            response = 'Number of People Online\n'
            found = False
            if '**chatlist' in msg:
                clientNo = 0
                for name in keys:
                    clientNo += 1
                    response = response + str(clientNo) +'::' + name+'\n'
                client.send(response.encode('ascii'))
            elif '**help' in msg:
                client.send(help.encode('ascii'))
            elif '**all' in msg:
                msg = msg.replace('**all','')
                for k,v in clients.items():
                    if k != uname:
                     v.send(msg.encode('ascii'))
            elif '**quit' in msg:
                response = 'Stopping Session and exiting...'
                client.send(response.encode('ascii'))
                clients.pop(uname)
                print(uname + ' has been logged out')
                clientConnected = False
            else:
                for name in keys:
                    if('**'+name) in msg:
                        msg = msg.replace('**'+name, '')
                        clients.get(name).send(msg.encode('ascii'))
                        found = True
                if(not found):
                    client.send('Trying to send message to invalid person.'.encode('ascii'))
        except:
            clients.pop(uname)
            print(uname + ' has been logged out')
            clientConnected = False


        


while serverRunning:
    #accept request and get the client and it's address 
    client, address = s.accept()
    #to send string to socket ==> send bytes 
    uname = client.recv(1024).decode('ascii')
    
    print('%s connected to the server'%str(uname))
    #welcome message
    client.send('Welcome to our chat room. Type **help to know all the commands'.encode('ascii'))
    
    if(client not in clients):
        clients[uname] = client
        threading.Thread(target = handleClient, args = (client, uname, )).start()
        
    