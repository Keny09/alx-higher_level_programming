#!/bin/bash
#Bash script that sends DELETE request to URL passed and  displays response
curl -sX DELETE -L "$1"
