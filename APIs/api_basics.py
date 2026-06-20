# APIs basics ---

# need to import (requests)

import requests

# Step -1 -The url
url = "https://official-joke-api.appspot.com/random_joke"

# Step -2 -Send request
response = requests.get(url)

# Step -3 -Did it work?
print(response.status_code)
# 200 = success, it worked
# 404 = not found
# 500 = server's own error

# Step -4 -See the reply (JSON)
print(response.text)
# this is just text, even though it LOOKS like a dict

# STEP -5 -Turn that response into actual python dictionary
data = response.json()
print(type(data))   # <class 'dict'>

# Now you can use like a normal dictionary
print(data["setup"])
print(data["punchline"])