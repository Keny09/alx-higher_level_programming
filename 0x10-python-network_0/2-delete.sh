#!/bin/bash
#Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
response=$(curl -s -X DELETE "$1"); echo "I'm a DELETE request"
