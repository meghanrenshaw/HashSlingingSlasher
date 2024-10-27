import requests
import hashlib
import sys
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")


def main():
    file_path = sys.argv[1]
    id = hash_file(file_path)
    url = f"https://www.virustotal.com/api/v3/files/{id}"

    headers = {"x-apikey": api_key}

    response = requests.get(url, headers=headers)

    print(response.text)


def hash_file(file_path):
    hash = hashlib.sha256()

    with open(file_path, "rb") as f:
        file_content = f.read()
        hash.update(file_content)

    return hash.hexdigest()


if __name__ == "__main__":
    main()
