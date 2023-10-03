import urllib.request
import urllib.error
import sys

def send_post_request(url, email):
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    try:
        with urllib.request.urlopen(url, data) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)