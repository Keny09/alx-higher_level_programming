import requests
import sys

# Check if a URL and email are provided as arguments
if len(sys.argv) < 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary containing the email parameter
data = {'email': email}

try:
    # Send a POST request to the URL with the email parameter
    response = requests.post(url, data=data)
    
    # Check for a successful response (status code 200)
    if response.status_code == 200:
        # Display the body of the response
        print(response.text)
    else:
        print(f"Error: Received status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print("Error:", e)
