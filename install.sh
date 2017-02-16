#! /bin/bash

echo -e "[\033[1;32mINFO:\033[0m] Start to install IPTV Agent"

# installation path of iptv agent, can be modified
installPath=/usr/local/IPTVAgent

echo -e  "[\033[1;32mINFO:\033[0m] Install prerequisite software"
installCentOS="yum -y install "
installUbuntu="apt-get -y install "
#install the dependent commands
SystemName=$(set `head -1 /etc/issue`;echo $1)
if (`test $SystemName = 'CentOS'`);then
$installCentOS "awk" 
$installCentOS "bc" 
$installCentOS "sed" 
$installCentOS "curl" 
$installCentOS "redis" 
echo
fi
if (`test $SystemName = 'Ubuntu'`);then
$installUbuntu "awk" 
$installUbuntu "bc" 
$installUbuntu "sed" 
$installUbuntu "curl" 
$installUbuntu "redis-server" 
fi 
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

echo -e "[\033[1;32mSTATUS:\033[0m] Install successfully"
