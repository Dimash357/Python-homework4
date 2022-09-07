import requests
import json

photo = requests.get(url="https://jsonplaceholder.typicode.com/photos")
print((photo.json()))


photos_list = photo.json()
for photo in photos_list:
    with open(f"json_photo/photo{photo['id']}.json", mode="w") as file:
        json.dump((photo), fp=file)



with open("photo.json", mode="rb") as file:
    json1 = json.load(file)
    print(json1)