import requests
import sys

# Check if repository name and owner name are provided as arguments
if len(sys.argv) < 3:
    print("Usage: python script.py <repository_name> <owner_name>")
    sys.exit(1)

repository_name = sys.argv[1]
owner_name = sys.argv[2]

# Define the GitHub API endpoint for listing commits
url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

try:
    # Send a GET request to the GitHub API
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        commits = response.json()
        # Limit the output to the 10 most recent commits
        for commit in commits[:10]:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: {response.status_code} - Failed to fetch commits.")
except requests.exceptions.RequestException as e:
    print("Error:", e)
