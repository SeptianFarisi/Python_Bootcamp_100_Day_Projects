import os
import requests
from datetime import datetime

NUTRITIONIX_ID = os.environ["NUTRITIONIX_ID"]
NUTRITIONIX_KEY = os.environ["NUTRITIONIX_KEY"]
sheet_url = os.environ["SHEET_URL"]
sheet_token = os.environ["SHEET_TOKEN"]

header = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_KEY,
}

host = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutrients_data = {
    "query": input("Tell me which exercises you did: ")
}

res = requests.post(url=f"{host}",params=header,json=nutrients_data)
data = res.json()
exercise = data["exercises"]
today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")
sheet_headers = {
    "Authorization": f"Bearer {sheet_token}"
}
if len(exercise) > 1:
    for _ in range(len(exercise)):
        name = exercise[_]["user_input"]
        duration = exercise[_]["duration_min"]
        calories = exercise[_]["nf_calories"]

        data_exercise = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": name.title(),
                "duration": duration,
                "calories": calories,
            }
        }
        sheet_res = requests.post(url=sheet_url,json=data_exercise,headers=sheet_headers)
        print(sheet_res.text)
else:
    name = exercise[0]["user_input"]
    duration = exercise[0]["duration_min"]
    calories = exercise[0]["nf_calories"]

    data_exercise = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": name.title(),
            "duration": duration,
            "calories": calories,
        }
    }
    sheet_res = requests.post(url=sheet_url, json=data_exercise, headers=sheet_headers)
    print(sheet_res.text)