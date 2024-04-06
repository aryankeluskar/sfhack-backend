import requests
import json

from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

import openai
from openai import OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

interests = []
interests.append("Hiking")
interests.append("Laser Tag")
interests.append("Hanging out")
interests.append("IKEA adventures")
interests.append("Furniture stores")
interests.append("Friends sitcom")
interests.append("Golden Gate Park")
interests.append("K Town")
interests.append("christopher nolan movies")
interests.append("watching ATP tennis")

prompt = f"based on these interests: {', '.join(interests)}. free time from 6pm to 11pm on tuesday and 9am to 3pm on thursday, what time do you recommend the group of 5 friends hang out for 3 hours. response only as 'day of week, morning or afternoon or evening or night, start time, end time; three random but inter-related common interests to explore' do not give any other text."
print(prompt)

print("-----------------")

fwclient = openai.OpenAI(
    base_url = "https://api.fireworks.ai/inference/v1",
    api_key=os.getenv("FIREWORKS_API_KEY"),
)
fwresponse = client.chat.completions.create(
  model="accounts/fireworks/models/mixtral-8x7b-instruct",
  messages=[{
    "role": "You can go through a list of big time slots and find only one time slot of 3 hours.",
    "content": prompt,
  }],
)

# previous implementation with OpenAI, now moved to Fireworks.ai
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You can go through a list of big time slots and find only one time slot of 3 hours."},
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message.content)

# times = "Tuesday evening, 6pm - 9pm; Hiking, Hanging out, Old city life."
times = completion.choices[0].message.content
hobbies = times.split(';')[1]
final_time = times.split(';')[0]
final_time = final_time.replace(",", " from ")
final_time = final_time.replace("-", " to ")
print("-----------------")
print(final_time)
print(hobbies)


print("-----------------")

promptPlans = f"{final_time}. group of 5 people who like {hobbies}. create an itienary for them to connect with each other and have fun. respond without any filler text, straightaway tell the itienary, include addresses and elaborate on details of locations in a way that responds to their emotions and potential for forming memories in San Francisco City"

completionPlans = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You make plans for new friends to discover each other. you focus on creating a sense of emotional belonging, and make sure the activities are such that they are done together in a group. focus on san francisco city."},
    {"role": "user", "content": promptPlans}
  ]
)

hangPlan = completionPlans.choices[0].message.content
print(hangPlan)

# response = requests.post(
#   url="https://openrouter.ai/api/v1/chat/completions",
#   headers={
#     "Authorization": f"Bearer {os.getenv('OPENROUTER')}",
#   },
#   data=json.dumps({
#     "model": "mistralai/mistral-7b-instruct:free", # Optional
#     "messages": [
#       {"role": "user", "content": f"{final_time}. group of 5 people who like {hobbies}. create an itienary for them to connect with each other and have fun. respond without any filler text, straightaway tell the itienary, include addresses and elaborate on details of locations in a way that responds to their emotions and potential for forming memories in San Francisco City"}
#     ]
#   })
# )