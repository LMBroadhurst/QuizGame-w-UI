import requests


THEME_COLOR = "#375362"
parameters = {
    "amount": 10,
    "type": "boolean"
}
URL = "https://opentdb.com/api.php"

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

data = response.json()
question_data = data["results"]
