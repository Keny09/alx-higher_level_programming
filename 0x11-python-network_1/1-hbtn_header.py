import urllib.request
import sys

def get_request_id(url):
    try:
        with urllib.request.urlopen(url) as response:
            headers = response.getheaders()
            for header in headers:
                if header[0] == 'X-Request-Id':
                    return header[1]
    except urllib.error.URLError as e:
        print(f"Failed to reach the server: {e.reason}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    request_id = get_request_id(url)

    if request_id:
        print(f"X-Request-Id: {request_id}")
    else:
        print("X-Request-Id not found in the response headers.")