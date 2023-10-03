import urllib.request

try:
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read().decode()
        print(body)
except urllib.error.URLError as e:
    print(f"Failed to reach the server: {e.reason}")
except Exception as e:
    print(f"An error occurred: {e}")