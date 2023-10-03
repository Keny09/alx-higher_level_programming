#!/bin/bash

# Check if the user provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL provided as an argument
url="$1"

# Send a request to the URL using curl and store the response in a variable
response=$(curl -s "$url")

# Get the size of the response body in bytes
response_size=$(echo -n "$response" | wc -c)

# Display the size of the response body
echo "$response_size"
