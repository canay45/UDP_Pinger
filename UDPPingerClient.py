from socket import *
from datetime import datetime


serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)


for e in range(10):
    sentTime = datetime.now()
    message = "Ping " + str(e+1) + " " + str(sentTime)

    try:
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        responseMessage, serverAddress = clientSocket.recvfrom(1024)
        RTT = datetime.now() - sentTime
        print(f'{responseMessage.decode()}, RTT: {RTT}')

    except Exception as e:
        print("Request timed out")

clientSocket.close()