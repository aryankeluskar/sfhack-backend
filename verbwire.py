import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

url = "https://api.verbwire.com/v1/nft/store/file"

fileUrl = "somefile.jpg"

files = { 
    "filePath": ( fileUrl , open(fileUrl, "rb"), "image/jpg") 
    }

headers = {
    "accept": "application/json",
    "X-API-Key": os.getenv("VERB_WIRE")
}

response = requests.post(url, files=files, headers=headers)
response = response.json()

print(response)
print(response['ipfs_storage']['ipfs_url'])