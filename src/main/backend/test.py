import requests

url = "http://127.0.0.1:8000/chatbot/"

request = requests.post(url, json={"message": "What's the weather like in Singapore?"})
print(request.json())