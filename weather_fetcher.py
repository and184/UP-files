import requests

API_KEY = "your_api_key_here"  # Замени на свой ключ
CITY = "Kyiv"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    temp = data['main']['temp']
    weather = data['weather'][0]['description']
    print(f"В {CITY} сейчас {temp}°C, {weather}")
else:
    print("Ошибка получения данных:", data)
