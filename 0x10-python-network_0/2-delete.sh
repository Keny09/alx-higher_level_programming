#!/bin/bash
#Bash script that sends DELETE request to URL passed and  displays response
response=$(curl -s -X DELETE "$1"); echo "I'm a DELETE request"
