#!/bin/bash
# Sends a POST request to the passed URL with the email and subject as parameters and displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" http://localhost:5000/send_email
