#!/bin/bash

# Get the URL from the command line arguments
url=$1

# Send a request to the URL
response=$(curl -s -o /dev/null -w "%{http_code}" $url)

# Display the status code of the response
echo $response