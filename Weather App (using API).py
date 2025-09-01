import requests
city = input("Enter city: ")
url = f"http://wttr.in/{city}?format=3"
print(requests.get(url).text)
