import requests

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=FNTvcOu9mSk4Aq2NafgIgZY93TWb2b5r6ctqWybN"

response = requests.get(url)

print(response.json())







