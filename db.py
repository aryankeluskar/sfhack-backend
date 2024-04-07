import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()


# Define the API endpoint URL
url = "https://us-west-2.aws.neurelo.com/rest/user"

# Define the headers with the X-API-KEY
headers = {
    "X-API-KEY": os.getenv("NEURELO")
}

# Make the GET request
response = requests.get(url, headers=headers)

# Get the response content
dbres = response.json()

# dump the response into db.json
with open("db.json", "w") as f:
    json.dump(dbres, f)

