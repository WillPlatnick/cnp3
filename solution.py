from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    recv = clientSocket.recv(1024).decode()
    # print(recv)

    # print(recv) #You can use these print statement to validate return codes from the server.
    # if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1) 
    # if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    clientSocket.send("MAIL FROM:<wp2132@nyu.edu>\r\n".encode())
    recv2 = clientSocket.recv(1024).decode()
    # print(recv2) 
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    clientSocket.send("RCPT TO:<wp2132@nyu.edu>\r\n".encode())
    recv3 = clientSocket.recv(1024).decode()
    # print(recv3) 
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    clientSocket.send("DATA\r\n".encode())
    recv4 = clientSocket.recv(1024).decode()
    # print(recv4) 

    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send("Subject: Totally Not Nigerian Spam\r\n\r\n".encode())
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv6 = clientSocket.recv(1024).decode()
    # print(recv6) 
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    clientSocket.send("QUIT\r\n".encode())
    recv7 = clientSocket.recv(1024).decode()
    # print(recv7)     # Fill in end

    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')