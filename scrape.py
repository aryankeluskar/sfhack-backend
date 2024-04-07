import os
from embedchain import App

from dotenv import load_dotenv
import json

import requests
load_dotenv()

from fastapi import FastAPI, Response, Cookie, Request

fast = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
fast.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your specific requirements
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

def newUser(twitter, linkedin, reddit, website):

    # name = "Aryan Keluskar"
    # bio = "attained from user"
    # age = 18

    # Replace this with your OpenAI key
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    app = App()
    # app.add("https://twitter.com/aryankeluskar6")
    # app.add("https://www.linkedin.com/in/aryankeluskar/")
    # app.add("https://www.reddit.com/user/Opposite_Volume117/")
    # app.add("https://aryankeluskar.github.io/")

    app.reset()

    app.add(twitter)
    app.add(linkedin)
    app.add(reddit)
    app.add(website)

    # app.add("https://www.instagram.com/aryankeluskar/")
    # app.add("https://github.com/aryankeluskar")
    interests = app.query(f"Generate a list of 10 interests of the given person that are separated by commas. make sure one is a hobby and one is a skill and one is a music artist. make sure none are too professional. make sure interests are 2-3 words and specific.")
    # Answer: The net worth of Elon Musk today is $258.7 billion.
    print(interests)
    interests = interests.split(",")
    fav = app.query(f"Based on what you find about the person and personality, what do you think would be his or her favourite places in San Francisco.")
    print(fav)

    url = "https://api.verbwire.com/v1/nft/store/file"

    fileUrl = "somefile.jpg"

    files = { 
        "filePath": ( fileUrl , open(fileUrl, "rb"), "image/jpg") 
        }

    headers = {
        "accept": "application/json",
        "X-API-Key": os.getenv("VERB_WIRE")
    }

    responsev = requests.post(url, files=files, headers=headers)
    responsev = responsev.json()

    verb = responsev['ipfs_storage']['ipfs_url']
    print(verb)

    # data = {
    #     "bio": bio,
    #     "dob": age,
    #     "favSF": fav,
    #     "interests": interests,
    #     "name": name,
    #     "pfp": verb,
    #     "sports": ["get from user"],
    # }

    # url = "https://us-west-2.aws.neurelo.com/rest/user/__one?"

    # headers = {
    #     "X-API-KEY": os.getenv("NEURELO")
    # }

    # response = requests.post(url, headers=headers, json=data)

    # print(response.json())

    # app.reset()

    return (interests, fav, verb)

@fast.get("/make")
async def root(tw = "", li = "", re = "", web = ""):
    (intarr, favsf, verb) = newUser(tw, li, re, web)
    return str(intarr)+";0;"+str(favsf)+";0;"+str(verb)