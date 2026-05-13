import pymysql  # Vaihdetaan kirjastoa
from flask import Flask, jsonify

app = Flask(__name__)


def hae_kentta(icao):
    try:
        # Huomaa hieman erilainen syntaksi pymysql:ssä
        yhteys = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password='SALASANA',
            cursorclass=pymysql.cursors.DictCursor  # Palauttaa tulokset sanakirjana
        )

        with yhteys.cursor() as kursori:
            sql = "SELECT name, municipality FROM airport WHERE ident=%s"
            kursori.execute(sql, (icao,))
            tulos = kursori.fetchone()

        yhteys.close()
        return tulos

    except Exception as e:
        # NYT näemme vihdoin sen oikean virheen!
        print(f"--- OIKEA VIRHE: {e} ---")
        return None


# Alkuluku-reitti pysyy samana...
@app.route('/alkuluku/<int:luku>')
def tarkista_alkuluku(luku):
    on_alkuluku = True
    if luku < 2:
        on_alkuluku = False
    else:
        for i in range(2, int(luku ** 0.5) + 1):
            if luku % i == 0:
                on_alkuluku = False
                break
    return jsonify({"Number": luku, "isPrime": on_alkuluku})


@app.route('/kenttä/<string:icao>')
def lentokentta_api(icao):
    tulos = hae_kentta(icao)
    if tulos:
        return jsonify({
            "ICAO": icao,
            "Name": tulos["name"],
            "Municipality": tulos["municipality"]
        })
    return jsonify({"error": "Airport not found or database error"}), 404


if __name__ == '__main__':
    app.run(port=3000)