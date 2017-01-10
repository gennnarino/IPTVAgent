#! /bin/bash
#terminate the current iptvm processes
./stop.sh
#remove iptvmCrond task
rm /etc/cron.d/iptvmCrond
#rm iptvm folder
rm -rf /etc/iptvm
