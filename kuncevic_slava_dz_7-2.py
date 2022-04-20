import json
import os

root = os.path.dirname(__file__)

with open('config.json', 'r', encoding='utf-8') as f:
    conf = json.load(f)

for dir_path in conf:
    full_dir_path = os.path.join(root, dir_path)
    os.makedirs(full_dir_path, exist_ok=True)
    for file_name in conf[dir_path]:
        with open(os.path.join(full_dir_path, file_name), 'x', encoding='utf-8'):
            pass
