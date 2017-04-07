class Parameter(object):
    """
    parameter setting
    """

    REQUEST = 0
    RESPONSE = 1
    
    # iptvstreaming operation
    STOP_IPTVSTREAMING = 1
    START_IPTVSTREAMING = 2
    RESTART_IPTVSTREAMING = 3

    # stream operation
    STOP_STREAM = 4
    START_STREAM = 5
    RESTART_STREAM = 6
    
    # mysql operation
    STOP_MYSQL = 7
    START_MYSQL = 8
    RESTART_MYSQL = 9
    
    # nginx operation
    STOP_NGINX = 10
    START_NGINX = 11
    RESTART_NGINX = 12
    
    # exit
    EXIT = 13

    def __init__(self):
        super(Parameter,self).__init__()

    @staticmethod
    def configParse(name):
        from ConfigParser import ConfigParser
        CONFIGFILE = '/usr/local/IPTVAgent/cfg/control.cfg'
        config = ConfigParser()
        config.read(CONFIGFILE)
        return config.get('python_control', name)

