#!/bin/bash
# Use curl to send a request and display the size of the body in bytes
curl -sI "$1" | grep -i "Content-Length" | cut -d ' ' -f2
