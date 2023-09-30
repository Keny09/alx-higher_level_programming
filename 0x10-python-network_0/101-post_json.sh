#!/bin/bash

# Get the URL and filename from the command line arguments
url=$1
filename=$2

# Read the contents of the file into a variable
file_contents=$(cat $filename)

# Send a POST request to the URL with the file contents in the body
response=$(curl -s -X POST -H "Content-Type: application/json" -d "$file_contents" $url)

# Display the body of the response
echo $response