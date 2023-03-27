from flask import Flask, jsonify
from utils import *

app = Flask(__name__)
app.config['ensure_ascii'] = False
app.config['JSON_SORT_KEYS'] = False

"""Вьюшка для поиска по названию"""


@app.route('/movie/<title>')
def get_movie_by_title(title):
    return movie_by_title(title)


"""Вьюшка для поиска по годам"""


@app.route('/movie/<int:year1>/to/<int:year2>')
def get_movie_by_years(year1, year2):
    return jsonify(movie_by_years(year1, year2))


"""Вьюшка для поиска по возрастной категории"""


@app.route('/rating/<age_category>')
def get_movie_by_rating(age_category):
    return jsonify(movie_by_rating(age_category))


"""Вьюшка для поиска по жанру"""


@app.route('/genre/<genre>')
def get_movie_by_genre(genre):
    return jsonify(movie_by_genre(genre))


if __name__ == "__main__":
    app.run(debug=True, port=1608)
