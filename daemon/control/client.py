## client for test
import socket
import json
from params import Parameter

HOST = '192.168.1.6'
PORT = 9000

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        cmd = raw_input("Please input your cmd:")
        s.send(cmd)
        cmd = json.loads(cmd)
        if cmd['command'] == Parameter.EXIT:
            break;
        data = s.recv(1024)
        print data
        data = json.loads(data)
        if data['status'] == 0:
            break
    s.close()

if __name__ == '__main__':
    main()
