import requests
import json

request = "https://api.tvmaze.com/search/shows?q=house"
response = requests.get(request) #.json()
if response.status_code == 200:

    dict0 = response.json()[0]
    score = dict0["score"]
    print(f"Score is {score}")

    dict1 = dict0["show"]
    print("URL: " + dict1["url"])
    print(dict1["genres"])
    for g in dict1["genres"]:
        print(g)

    print(response.json()[0]["show"]["genres"])

else:
    print(f"Error, status code is {response.status_code}")