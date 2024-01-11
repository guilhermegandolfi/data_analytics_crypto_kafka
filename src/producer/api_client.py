import requests

class APIClient:


    def __init__(self, url):
        self.url=url

    def get_request(self):
        try:
            url = self.url
            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except requests.exceptions.RequestException as err:
            print(f"An error occurred: {err}")      


if __name__ == "__main__":
    url = "https://api.blockchain.com/v3/exchange/tickers"
    api_client = APIClient(url)
    response = api_client.get_request()
    print(response)
