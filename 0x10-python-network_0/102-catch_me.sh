#!/bin/bash

# Make a request to the server
response=$(curl -s 0.0.0.0:5000/catch_me)

# Check if the response contains the message "You got me!"
if [[ $response == *"You got me!"* ]]; then
  echo "You got me!"
else
  echo "The server did not respond with the message 'You got me!'"
fi
