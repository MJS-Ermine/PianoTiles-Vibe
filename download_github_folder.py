import os
import requests
from typing import List

API_URL = "https://api.github.com/repos/MJS-Ermine/Python-Games/contents/Piano%20Tiles"
RAW_BASE = "https://raw.githubusercontent.com/MJS-Ermine/Python-Games/master/Piano%20Tiles"

HEADERS = {"User-Agent": "Mozilla/5.0"}

def download_from_github_api(api_url: str, local_dir: str) -> None:
    os.makedirs(local_dir, exist_ok=True)
    resp = requests.get(api_url, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    items = resp.json()
    for item in items:
        name = item['name']
        path = item['path']
        if item['type'] == 'file':
            raw_url = item['download_url']
            print(f"Downloading {raw_url} ...")
            r = requests.get(raw_url, headers=HEADERS, timeout=10)
            with open(os.path.join(local_dir, name), "wb") as f:
                f.write(r.content)
        elif item['type'] == 'dir':
            sub_api_url = f"https://api.github.com/repos/MJS-Ermine/Python-Games/contents/{path}"
            sub_local_dir = os.path.join(local_dir, name)
            download_from_github_api(sub_api_url, sub_local_dir)

if __name__ == "__main__":
    download_from_github_api(API_URL, "./Piano Tiles") 