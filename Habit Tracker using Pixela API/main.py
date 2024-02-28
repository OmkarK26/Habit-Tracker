import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

username = "omkarkamble"
token = "thisistopsecret"
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)


graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
headers = {
    "X-USER-TOKEN": "thisistopsecret"
}

graph_config = {
    "id": "graph1",
    "name": "Walking Data",
    "unit": "KM",
    "type": "float",
    "color": "shibafu",
}

response2 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

post_data = {
    "date": "20230126",
    "quantity": "15"
}
post_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1"
response3 = requests.post(url=post_endpoint, json=post_data, headers=headers)
print(response3)