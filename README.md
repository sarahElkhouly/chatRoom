# chatRoom
Sockets  is bi-directional, and establishes communication between a server and one or more clients. 
Here, we set up a socket on each end and allow a client to interact with other clients via the server.
The socket on the server side associates itself with some hardware port on the server side.
Any client that has a socket associated with the same port can communicate with the server.
We will require two scripts to establish this chat room. One to keep the serving running, 
and another that every client should run in order to connect to the server.
