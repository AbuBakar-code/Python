import requests
from datetime import datetime

USER_NAME = "abubakar-code"
TOKEN = "kjsdvfhequyrh9843jn"
ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
pixel_endpoint = f"{graph_endpoint}/{ID}"
today = datetime.now()
user_params = {
  "token": TOKEN,
  "username": USER_NAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes",
}

headers = {
  "X-USER-TOKEN": TOKEN
}

graph_config = {
  "id": ID,
  "name": "coding",
  "unit": "hours",
  "type": "int",
  "color": "sora",
}

post_pixel = {
  "date": today.strftime("%Y%m%d"),
  "quantity": "4"
}



# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

response = requests.post(url=pixel_endpoint, json=post_pixel, headers=headers)
print(response.text)