#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response (if status code is 200)

curl -s -o /dev/null -w "%{http_code}" "$1" | { read status_code; [ "$status_code" -eq 200 ] && curl -s "$1"; }

