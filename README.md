## Introduction

IPTVAgent is a agent tool,which can be used to gather system information, e.g. CPU,Memory,Load, and application status, e.g.nginx,mysql,etc. The results can be pushed to remote mysql server.It can also receive remote server's command and execute the command. Here are some functions of IPTVAgent:

* System information collection
* Process status information collection
* Web server status information collection
* Push all information to MySQL database
* Receive command and execute

## Installation

IPTVAgent is available on GitHub, you can clone and install it as follows:

  $ git clone https://github.com/LazarAngelov/IPTVAgent.git  
  $ cd IPTVAgent  
  $ ./install.sh  

After installation, you may see these files in /usr/local/IPTVAgent folder:

* iptvagent, is a control program;
* cfg/iptvagent.cfg, which is IPTVAgent's main configuration file;
* daemon/iptvagentd, is used to run IPTVAgent to collect realtime information every second;
* crond/iptvagent, is used to run IPTVAgent to collect detailed information every minute;
* lib/functions, is main function library used by IPTVAgent;
* moudules/*, collection programs

## Configuraion

* you can modify the installation path which is /usr/local/IPTVAgent by default in install.sh
* you should provide the remote and local mysql server's information in cfg/iptvagent.cfg 

## Usage

/usr/local/IPTVAgent start|stop|restart|status
