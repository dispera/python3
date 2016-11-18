import requests

print('this is a test')

request = requests.get("http://www.ezhome.com")

print(request.content)