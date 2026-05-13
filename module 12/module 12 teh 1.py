import requests

# API-osoite muuttujaan
pyynto = "https://api.chucknorris.io/jokes/random"

try:
    # Tehdään API-kutsu
    vastaus = requests.get(pyynto)

    # Tarkistetaan HTTP-statuskoodi (200 = onnistunut)
    if vastaus.status_code == 200:
        # Muunnetaan JSON-vastaus Python-sanakirjaksi
        json_vastaus = vastaus.json()

        # Tulostetaan vitsin teksti sanakirjasta
        print(json_vastaus["value"])
    else:
        print("Haku epäonnistui, statuskoodi:", vastaus.status_code)

except requests.exceptions.RequestException as e:
    # Virheenkäsittely, jos verkkoyhteys ei toimi
    print("Verkkovirhe vitsin hakemisessa.")