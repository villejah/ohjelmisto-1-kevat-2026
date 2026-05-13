import requests

# Käytetään annettua API-avainta
api_key = "c980a992f63a7092c626b0699083dc50"

# Kysytään kunnan nimi täsmälleen vaaditulla kehotteella
municipality = input("Enter municipality name: ")

# Muodostetaan hakukysely (units=metric takaa Celsius-asteet)
request_url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}&units=metric"

try:
    # Tehdään API-kutsu
    response = requests.get(request_url)

    # Tarkistetaan, että haku onnistui (HTTP 200)
    if response.status_code == 200:
        # Muunnetaan vastaus Python-sanakirjaksi
        data = response.json()

        # Poimitaan kuvaus ja lämpötila JSON-rakenteesta
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]

        # Tulostetaan tulokset täsmälleen vaaditussa muodossa
        print(f"Weather: {description}")
        print(f"Temperature: {temperature} Celsius")

    elif response.status_code == 404:
        print("Municipality not found.")
    else:
        print(f"Error fetching data. Status code: {response.status_code}")

except requests.exceptions.RequestException:
    print("Network error occurred.")