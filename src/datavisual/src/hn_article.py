import requests
import json
from pathlib import Path
from find_dir import find_dir as fd

path_fd = fd(1, 'data', 'readable_hn_article.json')
print(f"path_fd: {path_fd}")
path = Path(path_fd)


url = 'https://hacker-news.firebaseio.com/v0/item/31353677.json'
r = requests.get(url)
print(f"status code: {r.status_code}")
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
path.write_text(response_string)
print(response_string)  