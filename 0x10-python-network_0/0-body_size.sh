#!/bin/bash

# Check if the URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url="$1"

# Use curl to send a GET request and save the response body to a temporary file
response_file=$(mktemp)
curl -s -o "$response_file" "$url"

# Check if curl encountered any errors
if [ $? -ne 0 ]; then
  echo "Error: Failed to retrieve the URL: $url"
  rm -f "$response_file"
  exit 1
fi

# Get the size of the response body in bytes
response_size=$(wc -c < "$response_file")

# Display the size of the response body in bytes
echo "Size of the response body: $response_size bytes"

# Clean up the temporary response file
rm -f "$response_file"
