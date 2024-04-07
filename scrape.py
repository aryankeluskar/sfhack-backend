import os
from embedchain import App

from dotenv import load_dotenv
import json

import requests
load_dotenv()

# Replace this with your OpenAI key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = App()
# app.add("https://twitter.com/aryankeluskar6")
# app.add("https://www.linkedin.com/in/aryankeluskar/")
# app.add("https://www.reddit.com/user/Opposite_Volume117/")
# app.add("https://aryankeluskar.github.io/")


app.reset()

name = "Aryan Keluskar"
app.add("https://twitter.com/aryankeluskar6/")
app.add("https://www.linkedin.com/in/aryankeluskar")
app.add("https://www.reddit.com/user/Opposite_Volume117/")
app.add("https://aryankeluskar.github.io/")

# app.add("https://www.instagram.com/aryankeluskar/")
# app.add("https://github.com/aryankeluskar")
interests = app.query(f"Generate a list of 10 interests of {name} that are separated by commas. make sure one is a hobby and one is a skill and one is a music artist. make sure none are too professional. make sure interests are 2-3 words and specific.")
# Answer: The net worth of Elon Musk today is $258.7 billion.
print(interests)
interests = interests.split(",")
fav = app.query(f"Based on what you find about {name} and his personality, what do you think would be his favourite places in San Francisco.")
print(fav)

data = {
    "bio": "get from user",
    "dob": 17,
    "favSF": fav,
    "interests": interests,
    "name": name,
    "pfp": "get url from verbwire",
    "sports": ["get from user"],
}

# curl -X POST "https://us-west-2.aws.neurelo.com/rest/user/__one?" -H "X-API-KEY:neurelo_9wKFBp874Z5xFw6ZCfvhXSfHrdMTqOyuqTDVTrzG92wCHpFF8ISlY6sfj4R5TNb0rFm5RUHrLh2VxXEdAbRC/zH/O8ScerCu/L91fmaUYVjJ8+0x5rOh8JJg2d5N+4oA+XDJ2AEQ6LXkuL/686YSeClKgo2ppI5mnjJ5ZWc0uNmD5RsJ2kC7YiVMaecg8drX_iVgAvp3x7mjfQWaahWUDGBdlxCqXeu3q+20GzflpNtQ=" --json "{\r\n            \"bio\": \"Testing.\",\r\n            \"dob\": \"1990-08-09T22:51:56.000Z\",\r\n            \"favSF\": \"Nor\",\r\n            \"interests\": [\r\n                \"Alone Economy.\",\r\n                \"Either Push Force Such.\"\r\n            ],\r\n            \"name\": \"Jermaine Pratt DVM\",\r\n            \"pfp\": \"https://picsum.photos/441/597\",\r\n            \"sports\": [\r\n                \"Staff Gun Strategy Beat.\",\r\n                \"Energy Reach Indeed Amount.\"\r\n            ]\r\n        }"

url = "https://us-west-2.aws.neurelo.com/rest/user/__one?"

headers = {
    "X-API-KEY": os.getenv("NEURELO")
}

response = requests.post(url, headers=headers, json=data)

print(response.json())

app.reset()