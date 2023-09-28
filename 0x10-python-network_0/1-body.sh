#!/bin/bash
# Check if the URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the URL and store the response
response=$(curl -s -w "\n%{http_code}" "$1")

# Get the HTTP status code from the response
status_code=$(echo "$response" | tail -n1)

# Get the body of the response
body=$(echo "$response" | sed '$d')

# Display only the body of a 200 status code response
if [ "$status_code" -eq 200 ]; then
    echo "$body"
else
    echo "Request failed with status code $status_code"
fi
