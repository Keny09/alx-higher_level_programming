#!/bin/bash
# Sends a POST request to the passed URL with the email and subject as parameters and displays the body of the response
curl -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
