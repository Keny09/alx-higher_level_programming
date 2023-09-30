#!/bin/bash

# Check if the URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Set the URL and custom header value
url="$1"
header_value="98"

# Send a GET request with the custom header using curl
response=$(curl -s -H "X-School-User-Id: $header_value" "$url")

# Display the body of the response
echo "$response"
