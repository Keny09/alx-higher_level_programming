import requests
import sys

def fetch_request_id(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print ("Something went wrong", err)

    if response.status_code == 200:
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            print(f"The value of X-Request-Id is: {request_id}")
        else:
            print("The X-Request-Id header is not present in the response")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        fetch_request_id(url)
    else:
        print("Please provide a URL as a command line argument")