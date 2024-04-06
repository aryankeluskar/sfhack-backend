import os
from embedchain import App

from dotenv import load_dotenv
load_dotenv()

# Replace this with your OpenAI key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = App()
app.add("https://twitter.com/aryankeluskar6")
app.add("https://www.linkedin.com/in/aryankeluskar/")
app.add("https://www.reddit.com/user/Opposite_Volume117/")
app.add("https://aryankeluskar.github.io/")
# app.add("https://www.instagram.com/aryankeluskar/")
# app.add("https://github.com/aryankeluskar")
interests = app.query("Generate a list of 10 interests of Aryan Keluskar that are separated by commas. make sure one is a hobby and one is a skill and one is a music artist. make sure none are too professional. make sure interests are 2-3 words and specific.")
# Answer: The net worth of Elon Musk today is $258.7 billion.
print(interests)
fav = app.query("Based on what you find about Aryan Keluskar and his personality, what do you think would be his favourite places in San Francisco.")
print(fav)