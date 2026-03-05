import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="",
    autocommit=True
)

cursor = connection.cursor()

icao = input("Enter the ICAO code of an airport: ").upper()

sql = "SELECT name, municipality FROM airport WHERE ident=%s"
cursor.execute(sql, (icao,))

result = cursor.fetchone()


if result:
    print("Airport name:", result[0])
    print("Location:", result[1])
else:
    print(f"No airport found with ICAO code {icao}")