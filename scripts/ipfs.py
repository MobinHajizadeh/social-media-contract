import requests
import json


def upload_to_ipfs(file):
    # sample
    files = {
        "file": (file),
    }

    response = requests.post("https://ipfs.infura.io:5001/api/v0/add", files=files)

    p = response.json()
    hash = p["Hash"]

    print(f"File uploaded to IPFS!\nHASH: {hash}")
    return hash


def read_from_ipfs(hash):
    params = (("arg", hash),)

    response = requests.post(
        "https://ipfs.infura.io:5001/api/v0/cat",
        params=params,
    )

    print(response.text)
