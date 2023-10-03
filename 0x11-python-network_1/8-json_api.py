import requests
import sys

# Check if a letter is provided as an argument
if len(sys.argv) < 2:
    q = ""
else:
    q = sys.argv[1]

# Define the URL
url = "http://0.0.0.0:5000/search_user"

# Define the data payload with the 'q' parameter
data = {"q": q}

try:
    # Send a POST request to the URL with the 'q' parameter
    response = requests.post(url, data=data)
    
    # Check if the response body is JSON formatted and not empty
    if response.headers.get('content-type') == 'application/json':
        try:
            result = response.json()
            if result:
                user_id = result.get("id")
                user_name = result.get("name")
                print(f"[{user_id}] {user_name}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    else:
        print("No result")
except requests.exceptions.RequestException as e:
    print("Error:", e)
