# QUERY PARAMETERS — SENDING YOUR OWN INPUT TO AN API

# query parameters = extra info added to a URL to customize the request

import requests

# ============================================================
# THE MANUAL WAY — look at this URL pattern
# ============================================================
# https://api.agify.io/?name=samay
#                       ^^^^^^^^^^
#                       this part after the ? is a query parameter
# this API guesses someone's age based on their name

name = "samay"
url = f"https://api.agify.io/?name={name}"
response = requests.get(url)
data = response.json()

print(data)

print(f"{data['name']} is probably around {data['age']} years old")

# Cleaner way --- Insted of building the url string yourself using the params argument

url2 = "https://api.agify.io/"
params = {"name": "rahul"}
response2 = requests.get(url2, params=params)
data2 = response2.json()

print(data2)