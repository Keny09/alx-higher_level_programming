#!/usr/bin/python3
# Check if the URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Send a request to the URL and get the size of the body of the response
response_size=$(curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}')

# Check if the size is available
if [ -z "$response_size" ]; then
    echo "Failed to get the size of the response body."
else
    echo "The size of the response body is $response_size bytes."
fi
