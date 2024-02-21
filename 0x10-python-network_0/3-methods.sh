#!/bin/bash
# Query the server for allow HTTP methods and display the list
curl -sI -X OPTIONS "$1" | grep -i "Allow" | cut -d ' ' -f2-
