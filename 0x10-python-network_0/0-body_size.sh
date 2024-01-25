#!/bin/bash
# Check if url is provided s an argumrnt
if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit
fi

# Use curl to send a request and display the size of the body in bytes
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
