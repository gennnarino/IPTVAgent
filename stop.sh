#! /bin/bash
psCmd=`which ps`
grepCmd=`which grep`
awkCmd=`which awk`
killCmd=`which kill`
testCmd=`which test`
#remove iptvmCrond task
rm /etc/cron.d/iptvmCrond
#kill the remaining processes
PIDs=`$psCmd -ef|$grepCmd modules/realtime|$grepCmd -v "grep" | $awkCmd '{print $2}'`
if(`$testCmd -n "$PIDs"`); then
$killCmd $PIDs
fi
