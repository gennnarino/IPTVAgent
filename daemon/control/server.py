import socket
from params import Parameter
from handler import ConnectionThread

HOST = Parameter.configParse('localIP')
PORT = int(Parameter.configParse('localPort'))

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(5)
    except socket.error,e:
        print e
        s.close()
        return 1

    print 'Server start at: %s:%s' %(HOST, PORT)
    print 'Wait for connection...'

    while True:
        # accpet new connection
        sock, addr = s.accept()
        if addr[0] == HOST:
            sock.close()
            break 
        # create thread to handle the connection
        t = ConnectionThread(sock, addr)
        t.start()

    s.close()

if __name__ == '__main__':
    main()
