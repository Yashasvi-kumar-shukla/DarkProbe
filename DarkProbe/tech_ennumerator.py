import requests

class tech_ennumerator:
    def get_technologies_builtwith(target,key):
        api_key = key
        url = f"https://api.builtwith.com/v14/api.json?KEY={api_key}&LOOKUP={target}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else "Error fetching technologies"