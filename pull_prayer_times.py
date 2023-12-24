# %%
from cred import *
import httpx
import json
import datetime

# %%
# Get the current date and time
now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")

# %%
# Get the prayer times
url = 'https://www.londonprayertimes.com/api/times/?format=json&24hours=true&key=' + APIKEY
r = httpx.get(url)

# %%
data = r.json()
print(data)


