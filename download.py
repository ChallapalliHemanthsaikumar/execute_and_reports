#!usr/bin/env python
import requests


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


download("https://i.pinimg.com/736x/cf/ab/a8/cfaba87af566c1f5a44efe6f5f17d155.jpg")
