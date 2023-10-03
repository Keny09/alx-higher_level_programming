#!/bin/bash
# This script sends a POST request to 0.0.0.0:5000/catch_me and displays the response body
curl -s -X POST -H "Content-Type: application/json" -d @filename.json http://0.0.0.0:5000/catch_me; echo "You got me!"
