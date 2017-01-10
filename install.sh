#! /bin/bash
echoCmd=`which echo`
headCmd=`which head`
testCmd=`which test`
installCentOS="yum -y install "
installUbuntu="apt-get -y install "
#install the dependent commands
SystemName=$(set `$headCmd -1 /etc/issue`;$echoCmd $1)
if(`$testCmd $SystemName = 'CentOS'`);then
$installCentOS "awk" &
$installCentOS "bc" &
$installCentOS "sed" &
$installCentOS "curl" &
$installCentOS "redis" &
echo
fi
if(`$testCmd $SystemName = 'Ubuntu'`);then
$installUbuntu "awk" &
$installUbuntu "bc" &
$installUbuntu "sed" &
$installUbuntu "curl" &
$installUbuntu "redis" &
fi 
#mkdir for iptvm
mkdir -p /etc/iptvm/modules
#copy modules 
cp modules/* /etc/iptvm/modules/
find /etc/iptvm/modules/ -type f -exec chmod 744 {} \;
#add iptvmCrond to /etc/cron.d
cp iptvmCrond /etc/cron.d/
chmod 644 /etc/cron.d/iptvmCrond
