import socket
from params import Parameter
from handler import ConnectionThread

HOST = Parameter.configParse('localIP')
PORT = int(Parameter.configParse('localPort'))

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    print 'Server start at: %s:%s' %(HOST, PORT)
    print 'Wait for connection...'

    while True:
        # accpet new connection
        sock, addr = s.accept()
         
        # create thread to handle the connection
        t = ConnectionThread(sock, addr)
        t.start()

if __name__ == '__main__':
    main()
