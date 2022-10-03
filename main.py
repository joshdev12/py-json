import requests

URL = "https://cdn.punchng.com/wp-content/uploads/2022/08/14023815/Olaniyi-Afonja.jpg"

img = requests.get(URL)

# print(img.content)

with open("afonja.jpg", mode="bw") as file:
    file.write(img.content)