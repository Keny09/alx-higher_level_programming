import requests

def fetch_status():
    url = "https://alx-intranet.hbtn.io/status"

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
        print(response.text)

if __name__ == "__main__":
    fetch_status()