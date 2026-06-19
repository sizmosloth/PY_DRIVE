# CALLING A REAL API — GITHUB'S API

import requests   # this is what actually talks to the internet
import json

username = "sizmosloth"

url = f"https://api.github.com/users/{username}"

# Making the request ---

response = requests.get(url)
# 200 = success
# 404 = user not found
# this is how every API tells you whether it worked

# RAW JSON TEXT — what actually came back over the internet
print(response.text[:300])