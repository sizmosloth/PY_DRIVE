# HANDLING API FAILURES — things WILL go wrong eventually

# real apps don't assume the internet always works.
# wifi drops, servers go down, you type a typo in a URL — handle it.

import requests
# CASE 1 — BAD STATUS CODE (server responded, but said "no")

url = "https://api.github.com/users/this_user_does_not_exist_99999"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data["name"])
else:
    print(f"Something went wrong — status code: {response.status_code}")
    # 404 here = user not found, server still replied properly