from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # === Fill in start ===
    # Create socket and connect to the mail server
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # === Fill in end ===

    recv = clientSocket.recv(1024).decode()
    # print(recv)

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)

    # === Fill in start ===
    # Send MAIL FROM command and handle server response.
    mailFrom = 'MAIL FROM:<alice@example.com>\r\n'
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    # print(recv2)
    # === Fill in end ===

    # === Fill in start ===
    # Send RCPT TO command and handle server response.
    rcptTo = 'RCPT TO:<bob@example.com>\r\n'
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    # print(recv3)
    # === Fill in end ===

    # === Fill in start ===
    # Send DATA command and handle server response.
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    # print(recv4)
    # === Fill in end ===

    # === Fill in start ===
    # Send message data.
    clientSocket.send(msg.encode())
    # === Fill in end ===

    # === Fill in start ===
    # Message ends with a single period, send message end and handle server response.
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    # print(recv5)
    # === Fill in end ===

    # === Fill in start ===
    # Send QUIT command and handle server response.
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    # print(recv6)
    # === Fill in end ===

    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
