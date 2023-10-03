import requests
import sys

# Check if a username and personal access token are provided as arguments
if len(sys.argv) < 3:
    print("Usage: python script.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]

# Define the GitHub API endpoint for user information
url = f"https://api.github.com/user"

try:
    # Set up the authentication headers using Basic Authentication
    auth = (username, token)
    
    # Send a GET request to the GitHub API
    response = requests.get(url, auth=auth)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info["id"]
        print(f"GitHub User ID: {user_id}")
    else:
        print(f"Error: {response.status_code} - Failed to fetch user information.")
except requests.exceptions.RequestException as e:
    print("Error:", e)
