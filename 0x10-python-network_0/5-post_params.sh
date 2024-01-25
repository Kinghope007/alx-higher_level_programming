#!/bin/bash
# Use curl to send a POST request with paramter and display the body
curl -sL -X POST -d 'email=test%40gmail.com&subject=I+will+always+be+here+for+PLD' "$1"
