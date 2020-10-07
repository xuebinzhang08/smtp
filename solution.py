Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@xuebinzhang08 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


lzurzolo
/
cs-gy-6843-smtp
1
00
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
cs-gy-6843-smtp/solution.py /
@lzurzolo
lzurzolo Submission completed
Latest commit da784ae 6 days ago
 History
 1 contributor
75 lines (63 sloc)  2.23 KB
  
from socket import *

def smtp_client(port=1025, mailserver='127.0.0.7'):
    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFrom = "MAIL FROM:<foobar>\r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptTo = "RCPT TO:<lorenzo@blarghblahblargh.com>\r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataHeader = "DATA\r\n"
    clientSocket.send(dataHeader.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4)
    # Fill in end

    # Send message data.
    # Fill in start
    subject = "Subject: Hi this is a test e-mail subject from my client\r\n\r\n"
    clientSocket.send(subject.encode())
    msg = "\r\n I sure hope this works"
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    end = "\r\n.\r\n"
    clientSocket.send(end.encode())
    recv5 = clientSocket.recv(1024).decode()
    #print(recv5)
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitMsg = "QUIT\r\n"
    clientSocket.send(quitMsg.encode())
    recv6 = clientSocket.recv(1024).decode()
    #print(recv6)
    # Fill in end

if __name__ == '__main__':
    smtp_client(1025, "127.0.0.7")
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
