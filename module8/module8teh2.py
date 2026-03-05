import mysql.connector

def get_airports_by_country(country_code):
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",
        user="root",
        password="",
        autocommit=True
    )
    cursor = connection.cursor()
    sql = """
    SELECT type, COUNT(*)
    FROM airport
    WHERE iso_country = %s
    GROUP BY type
    ORDER BY COUNT(*) DESC
    """
    cursor.execute(sql, (country_code,))
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def run_country_program():
    country_code = input("Enter the country code (e.g., FI for Finland): ")
    country_code = country_code.upper()

    airports = get_airports_by_country(country_code)

    if airports:
        print("\n")
        print(f"Airports in {country_code}:")
        for airport_type, count in airports:
            print(f"{count} {airport_type} airports")
    else:
        print(f"No airports found for country code '{country_code}'.")

run_country_program()