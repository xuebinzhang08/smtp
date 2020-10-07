from socket import *
import base64


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()


    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFrom = 'MAIL FROM:<1234@qqq.com>\r\n'
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    reptTo = 'RCPT TO:<1234@qqq.com>\r\n'
    clientSocket.send(reptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg)
    recv6 = clientSocket.recv(1024).decode()
    # print(recv6)
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quit = 'QUIT\r\n'
    clientSocket.send(quit.encode())
    recv7 = clientSocket.recv(1024).decode()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
