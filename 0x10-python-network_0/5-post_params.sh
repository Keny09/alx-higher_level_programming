#!/bin/bash

# Check if the URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Define the URL and the data to send
url="$1"
data="email=test@gmail.com&subject=I will always be here for PLD"

# Send a POST request and display the body of the response
response=$(curl -s -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "$data" "$url")
echo "$response"