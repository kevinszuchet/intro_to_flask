import os
from flask import Flask, request, jsonify


app = Flask(__name__)

cities = []


@app.route('/cities')
def get_cities():
    limit, offset = request.args.get('limit'), request.args.get('offset')
    output = cities[offset:] if offset else cities
    output = output[:limit] if limit else output
    return jsonify(output)


@app.route('/cities/<int:city_id>')
def get_city(city_id):
    return next((city for city in cities if city['id'] == city_id), None)


@app.post('/cities')
def create_city():
    # It expects the city object as {name, country, continent, rank, cost, internet, fun, safety}
    city = request.json
    print("new city", city)
    cities.append(city)
    return {}, 201


@app.route('/cities/rank')
def rank():
    sort_by = request.args.get('sort_by') or 'rank'
    return sorted(cities, key=lambda city: city[sort_by], reverse=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT')))
