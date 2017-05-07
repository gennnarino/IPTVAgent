import socket
from params import Parameter
from handler import ConnectionProcess

HOST = Parameter.configParse('localIP')
PORT = int(Parameter.configParse('localPort'))

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
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
        p = ConnectionProcess(sock, addr)
        p.start()

    s.close()

if __name__ == '__main__':
    main()
