#! /bin/bash

installSoftware() {
    if [ $1 = redis ]; then
        soft=`which redis-server 2>&1`
    else
        soft=`which $1 2>&1`
    fi
    if [ $? -eq 0 ]; then
        return
    fi
    echo -e "[\033[1;32mINFO:\033[0m] Install $1 ..."
    system=$(head -1 /etc/issue|awk '{print $1}')
    if [ $system = CentOS ]; then
        yum -y install $1
    elif [ $system = Ubuntu ]; then
        if [ $1 = redis ]; then
            apt-get -y install redis-server
        else
            apt-get -y install $1
        fi
    else
        echo -e "[\033[1;31mWARNING:\033[0m] you should install $1 by yourself"
    fi
}

echo -e "[\033[1;32mINFO:\033[0m] Start to install IPTV Agent"

# installation path of iptv agent, can be modified
installPath=/usr/local/IPTVAgent

#mkdir for iptvagent
if [ ! -d $installPath ]; then
    mkdir -p $installPath
fi

echo -e "[\033[1;32mINFO:\033[0m] Copy iptvagent service to $installPath"
cp iptvagent $installPath

echo -e "[\033[1;32mINFO:\033[0m] Copy iptvagent subdir to $installPath"
cp -r lib/ cfg/ daemon/ crond/ modules/ $installPath

echo -e "[\033[1;32mINFO:\033[0m] Replace the path with $installPath"
sed -i "s%/usr/local/IPTVAgent%$installPath%g" `grep /usr/local/IPTVAgent -rl $installPath`
sed -i "s%/usr/local/IPTVAgent%$installPath%g" uninstall.sh

#find /etc/iptvm/modules/ -type f -exec chmod 744 {} \;

echo -e  "[\033[1;32mINFO:\033[0m] Install prerequisite software"
#install the dependent commands
installSoftware awk 
installSoftware sed 
installSoftware bc 
installSoftware curl 

echo -e "[\033[1;32mSTATUS:\033[0m] Install successfully"
