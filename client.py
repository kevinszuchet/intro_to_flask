import requests

uri = "http://localhost:5000"


def main():
    new_city = {
        "name": "Buenos Aires",
        "country": "Argentina",
        "continent": "South America",
        "rank": 20,
        "cost": 5,
        "internet": 4,
        "fun": 5,
        "safety": 3
    }
    res = requests.post(f"{uri}/cities", json=new_city)
    print(f"{res.status_code} POST")

    cities = requests.get(f"{uri}/cities")
    print(cities.json())


if __name__ == '__main__':
    main()
