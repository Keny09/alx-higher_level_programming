bash
#!/bin/bash

# Check if the URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Define the URL and the header variable
url="$1"
header="X-School-User-Id: 98"

# Send a GET request to the URL with the header variable and display the body of the response
response=$(curl -s -X GET -H "$header" "$url")
echo "$response"