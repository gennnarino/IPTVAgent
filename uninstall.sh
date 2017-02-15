#! /bin/bash

installPath=/usr/local/IPTVAgent

#terminate the current iptvagent process
count=`ps -ef|grep iptvagentd|grep -v grep|wc -l`
if [ $count -ne 0 ]; then
    echo -e "[\033[1;32mINFO:\033[0m] Stop iptvagent..."
    $installPath/iptvagent stop
fi

echo -e "[\033[1;32mINFO:\033[0m] Uninstall iptv agent..."

#remove deployed iptvagent
if [ -d $installPath ]; then
    rm -rf $installPath
fi

echo -e "[\033[1;32mSTATUS:\033[0m] uninstall successfully"
