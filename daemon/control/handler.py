import multiprocessing
import datetime
import json
from params import Parameter
import subprocess
import commands

class ConnectionProcess(multiprocessing.Process):
    """
    Receive data from client and send the response
    """

    def __init__(self, sock, addr):
        """
        Constructor

        @param sock client socket
        @param addr client address
        @param lock mutex lock
        """
        super(ConnectionProcess, self).__init__()
        self.sock = sock
        self.addr = addr
    
    def sendData(self, info):
        """
        send response data to client
        info [command, status, description]
        """
        data = {
            'action' : Parameter.RESPONSE,
            'command' : info[0],
            'status' : info[1],
            'description' : info[2]
        }
        data = json.dumps(data)
        self.sock.send(data)
        if info[1] == 0:
            self.sock.close()

    def getOS(self):
        result = commands.getstatusoutput("head -1 /etc/issue | awk '{print $1}'")
        if result[0] == 0:
            return result[1]
        else:
            return 'Unknown'

    def getstatusoutput(self, cmd):
        status = subprocess.call(cmd, shell=True)
        if status == 0:
            return (status, '')
        else:
            return commands.getstatusoutput(cmd)

    def executeCmd(self, protocol):
        """
        execute the corresponding command
        """
        if 'action' in protocol:
            action = protocol['action']
        if 'command' in protocol:
            command = protocol['command']
        if 'executor' in protocol:
            executor = protocol['executor']

        logPath = Parameter.configParse('controlLogPath')
        log = open(logPath, 'a')
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if action == Parameter.REQUEST:
    	    if command == Parameter.STOP_IPTVSTREAMING:
                streamingPath = Parameter.configParse('streamingPath')
                result = self.getstatusoutput(streamingPath+'/iptvstreaming stop')
                status = result[0]
                if status == 0:
                    print >> log, ('[%s] [INFO] [%s] successfully stopped iptvstreaming' % (now, executor))
                    self.sendData([command, 1, 'successfully stopped iptvstreaming'])
                else:
                    print >> log, ('[%s] [INFO] [%s] failed to stop iptvstreaming' % (now, executor))
                    self.sendData([command, 0, result[1]])
            elif command == Parameter.START_IPTVSTREAMING:
                streamingPath = Parameter.configParse('streamingPath')
                result = self.getstatusoutput(streamingPath+'/iptvstreaming start')
                status = result[0]
                if status == 0:
                    print >> log, ('[%s] [INFO] [%s] successfully started iptvstreaming' % (now, executor))
                    self.sendData([command, 1, 'successfully started iptvstreaming'])
                else:
                    print >> log, ('[%s] [INFO] [%s] failed to start iptvstreaming' % (now, executor))
                    self.sendData([command, 0, result[1]])
            elif command == Parameter.RESTART_IPTVSTREAMING:
                streamingPath = Parameter.configParse('streamingPath')
                result = self.getstatusoutput(streamingPath+'/iptvstreaming restart')
                status = result[0]
                if status == 0:
                    print >> log, ('[%s] [INFO] [%s] successfully restarted iptvstreaming' % (now, executor))
                    self.sendData([command, 1, 'successfully restarted iptvstreaming'])
                else:
                    print >> log, ('[%s] [INFO] [%s] failed to restart iptvstreaming' % (now, executor))
                    self.sendData([command, 0, result[1]])
            elif command == Parameter.STOP_STREAM:
                streamingPath = Parameter.configParse('streamingPath')
                streamName = protocol['streamName']
                result = self.getstatusoutput(streamingPath+'/iptvstreaming stopStream '+streamName)
                status = result[0]
                if status == 0:
                    print >> log, ('[%s] [INFO] [%s] successfully stopped stream %s' % (now, executor, streamName))
                    self.sendData([command, 1, 'successfully stopped stream '+streamName])
                else:
                    print >> log, ('[%s] [INFO] [%s] failed to stop stream %s' % (now, executor, streamName))
                    self.sendData([command, 0, result[1]])
    	    elif command == Parameter.START_STREAM:
                streamingPath = Parameter.configParse('streamingPath')
                streamName = protocol['streamName']
                result = self.getstatusoutput(streamingPath+'/iptvstreaming startStream '+streamName) 
                status = result[0]
                if status == 0:
                    print >> log, ('[%s] [INFO] [%s] successfully started stream %s' % (now, executor, streamName))
                    self.sendData([command, 1, 'successfully started stream '+streamName])
                else:
                    print >> log, ('[%s] [INFO] [%s] failed to start stream %s' % (now, executor, streamName))
                    self.sendData([command, 0, result[1]])
            elif command == Parameter.RESTART_STREAM:
                streamingPath = Parameter.configParse('streamingPath')
                streamName = protocol['streamName']
                result = self.getstatusoutput(streamingPath+'/iptvstreaming restartStream '+streamName)
                status = result[0]
                if status == 0:
                    print >> log, ('[%s] [INFO] [%s] successfully restarted stream %s' % (now, executor, streamName))
                    self.sendData([command, 1, 'successfully restarted stream '+streamName])
                else:
                    print >> log, ('[%s] [INFO] [%s] failed to restart stream %s' % (now, executor, streamName))
                    self.sendData([command, 0, result[1]])
            elif command == Parameter.STOP_MYSQL:
                system = self.getOS()
                if system == 'CentOS':
                    result = self.getstatusoutput('service mysqld stop')
                elif system == 'Ubuntu':
                    result = self.getstatusoutput('service mysql stop')
                else:
                    self.sendData([command, 0, 'unknown system, please execute command on the server'])
                    return 1
                status = result[0]
                if status == 0:
                    print >> log, ('[%s] [INFO] [%s] successfully stopped mysql' % (now, executor))
                    self.sendData([command, 1, 'successfully stopped mysql'])
                else:
                    print >> log, ('[%s] [INFO] [%s] failed to stop mysql' % (now, executor))
                    self.sendData([command, 0, result[1]])
            elif command == Parameter.START_MYSQL:
                system = self.getOS()
                if system == 'CentOS':
                    result = self.getstatusoutput('service mysqld start')
                elif system == 'Ubuntu':
                    result = self.getstatusoutput('service mysql start')
                else:
                    self.sendData([command, 0, 'unknown system, please execute command on the server'])
                    return 1
                status = result[0]
                if status == 0:
                    print >> log, ('[%s] [INFO] [%s] successfully started mysql' % (now, executor))
                    self.sendData([command, 1, 'successfully started mysql'])
                else:
                    print >> log, ('[%s] [INFO] [%s] failed to start mysql' % (now, executor))
                    self.sendData([command, 0, result[1]])
            elif command == Parameter.RESTART_MYSQL:
                system = self.getOS()
                if system == 'CentOS':
                    result = self.getstatusoutput('service mysqld restart')
                elif system == 'Ubuntu':
                    result = self.getstatusoutput('service mysql restart')
                else:
                    self.sendData([command, 0, 'unknown system, please execute command on the server'])
                    return 1
                status = result[0]
                if status == 0:
                    print >> log, ('[%s] [INFO] [%s] successfully restarted mysql' % (now, executor))
                    self.sendData([command, 1, 'successfully restarted mysql'])
                else:
                    print >> log, ('[%s] [INFO] [%s] failed to restart mysql' % (now, executor))
                    self.sendData([command, 1, result[1]])
            elif command == Parameter.STOP_NGINX:
                nginxPath = Parameter.configParse('nginxPath')
                result = self.getstatusoutput(nginxPath+'/sbin/nginx -s stop')
                status = result[0]
                if status == 0:
                    print >> log, ('[%s] [INFO] [%s] successfully stopped nginx' % (now, executor))
                    self.sendData([command, 1, 'successfully stopped nginx'])
                else:
                    print >> log, ('[%s] [INFO] [%s] failed to stop nginx' % (now, executor))
                    self.sendData([command, 0, result[1]])
            elif command == Parameter.START_NGINX:
                nginxPath = Parameter.configParse('nginxPath')
                result = self.getstatusoutput(nginxPath+'/sbin/nginx')
                status = result[0]
                if status == 0:
                    print >> log, ('[%s] [INFO] [%s] successfully started nginx' % (now, executor))
                    self.sendData([command, 1, 'successfully started nginx'])
                else:
                    print >> log, ('[%s] [INFO] [%s] failed to start nginx' % (now, executor))
                    self.sendData([command, 0, result[1]])
            elif command == Parameter.RESTART_NGINX:
                nginxPath = Parameter.configParse('nginxPath')
                result = self.getstatusoutput(nginxPath+'/sbin/nginx -s reload')
                status = result[0]
                if status == 0:
                    print >> log, ('[%s] [INFO] [%s] successfully restarted nginx' % (now, executor))
                    self.sendData([command, 1, 'successfully restarted nignx'])
                else:
                    print >> log, ('[%s] [INFO] [%s] failed to restart nginx' % (now, executor))
                    self.sendData([command, 0, result[1]])
            elif command == Parameter.EXIT:
                self.sock.close()
                status = 1
            else:
                self.sendData([command, 0, 'undefined command'])
                status = 1
        else:
            self.sendData([command, 0, 'invalid action'])
            status = 1

        log.close()
        return status

    def handle(self):
        """
        thread handle function
        """
        print 'Accpet new connection from %s:%s...' % self.addr
        while True:
    	    data = self.sock.recv(1024)
            print data
            try:
    	        protocol = json.loads(data)
            except Exception as e:
                self.sendData([0, 0, e.message])
                break
            status = self.executeCmd(protocol)
            if status != 0:
                break

    def run(self):
        """
        thread execute run method by default
        """
        self.handle()


