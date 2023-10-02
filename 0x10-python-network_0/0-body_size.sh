#!/bin/bash

# Check if the URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url="$1"

# Use curl with -s (silent mode) to send a GET request and save the response body to a variable
response_body=$(curl -s "$url")

# Check if curl encountered any errors
if [ $? -ne 0 ]; then
  echo "Error: Failed to retrieve the URL: $url"
  exit 1
fi

# Get the size of the response body in bytes
response_size=$(echo -n "$response_body" | wc -c)

# Display the size of the response body in bytes
echo "$response_size"

