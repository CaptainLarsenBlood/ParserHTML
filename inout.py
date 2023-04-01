from urllib.parse import urlparse
import os
import requests


def get_text(url: str) -> str:

    resp = requests.get(url=url)
    resp.raise_for_status()
    return resp.text


def save_txt(text: str, url: str):

    path_save = "Article/"+urlparse(url).netloc+urlparse(url).path
    os.makedirs(path_save, exist_ok=True)

    with open(f"{path_save}/index.txt", 'w+', encoding='utf-8') as file:
        file.write(str(text))
