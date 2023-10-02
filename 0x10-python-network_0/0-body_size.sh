#!/bin/bash

# Check if the URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url="$1"

# Use curl to send a GET request and retrieve the response body
response_body=$(curl -sI "$url" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')

# Check if curl encountered any errors
if [ $? -ne 0 ]; then
  echo "Error: Failed to retrieve the URL: $url"
  exit 1
fi

# Display the size of the response body in bytes
echo "$response_body"
