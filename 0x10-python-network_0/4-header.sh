#!/bin/bash
# Use curl to send a GET request with a custom header and display the body
curl -sL -H 'X-School-User-Id: 89' "$1"
