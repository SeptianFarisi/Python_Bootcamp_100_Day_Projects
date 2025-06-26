import requests
from datetime import datetime

TOKEN = "asdflkjgasdfkjasdfkdfssdf"
USERNAME = "septian"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# res = requests.post(pixela_endpoint,json=user_params)
# print(res.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

header = {
    "X-USER-TOKEN": TOKEN
}
GRAPH1 = "graph1"
graph_params = {
    "id": GRAPH1,
    "name": "Cycling",
    "unit": "Km",
    "type": "float",
    "color": "momiji",
    "timezone": "Asia/Jakarta",
}

# res = requests.post(url=graph_endpoint,json=graph_params,headers=header)
# print(res.text)

times = datetime.now()
time_format = times.strftime("%Y%m%d")

pixel_endpoint = f"{graph_endpoint}/{GRAPH1}"

pixel_config = {
    "date": time_format,
    "quantity": input("how many kilometers today: ")
}

# res = requests.post(url=pixel_endpoint,headers=header,json=pixel_config)
# print(res.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH1}/{time_format}"

pixel_update_data = {
    "quantity": input("how many kilometers: ")
}

# res = requests.put(url=pixel_update_endpoint,headers=header,json=pixel_update_data)
# print(res.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH1}/{time_format}"

# res = requests.delete(url=pixel_delete_endpoint,headers=header)
# print(res.text)