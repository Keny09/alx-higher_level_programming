import urllib.request
import urllib.parse
import sys

# Check if a URL and email are provided as arguments
if len(sys.argv) < 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Encode the email parameter
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

try:
    # Send a POST request to the URL with the email parameter
    with urllib.request
