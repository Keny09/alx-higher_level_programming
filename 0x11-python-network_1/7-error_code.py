import requests
import sys

# Check if a URL is provided as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Display the body of the response
    print(response.text)
    
    # Check the HTTP status code
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print("Error:", e)
