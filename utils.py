import sqlite3
from collections import Counter
from config import DB_PATH


def execute_query(query, path):
    """Подключение к базе данных"""
    with sqlite3.connect(path) as connection:
        cursor = connection.cursor()
        result = cursor.execute(query)
    return result


def movie_by_title(title):
    """Поиск фильма по названию"""
    query = f"""
            SELECT title, country, release_year, listed_in, description
            FROM netflix
            WHERE title LIKE '%{title}%'
            ORDER BY release_year DESC
            LIMIT 1
            """
    execute = execute_query(query, DB_PATH)
    result = execute.fetchone()
    if result is None:
        return "Не удалось найти фильм, попробуйте другой запрос"
    return {
        "title": result[0],
        "country": result[1],
        "release_year": result[2],
        "genre": result[3],
        "description": result[4]
    }


def movie_by_years(year1, year2):
    """Сортировка фильмов по годам"""
    query = f"""
            SELECT title, release_year
            FROM netflix
            WHERE release_year BETWEEN {year1} AND {year2}
            LIMIT 100
            """
    execute = execute_query(query, DB_PATH)
    result = execute.fetchall()
    result_list = []
    for movie in result:
        result_list.append({
            "title": movie[0],
            "release_year": movie[1]
        })
    return result_list


def movie_by_rating(rating):
    """Сортировка фильмов по возрастной категории"""
    rating_parameters = {
        "children": "'G'",
        "family": "'G', 'PG', 'PG-13'",
        "adult": "'R', 'NC-17'"
    }
    query = f"""
            SELECT title, rating, description
            FROM netflix
            WHERE rating in ({rating_parameters[rating]})
            """

    execute = execute_query(query, DB_PATH)
    result = execute.fetchall()
    result_list = []
    for movie in result:
        result_list.append({
            "title": movie[0],
            "rating": movie[1],
            "description": movie[2]
        })
    return result_list


def movie_by_genre(genre):
    """Сортировка по жанру"""
    query = f"""
            SELECT title, description
            FROM netflix
            WHERE listed_in LIKE '%{genre}%'
            ORDER BY release_year DESC
            LIMIT 10
            """
    execute = execute_query(query, DB_PATH)
    result = execute.fetchall()
    result_list = []
    for movie in result:
        result_list.append({
            "title": movie[0],
            "description": movie[1]
        })
    return result_list


def cast_partners(actor1, actor2):
    """Подбор актёров которые играют в паре"""
    query = f"""
            SELECT netflix.cast
            FROM netflix
            WHERE netflix.cast LIKE '%{actor1}%'
            AND netflix.cast LIKE '%{actor2}%'
            """
    execute = execute_query(query, DB_PATH)
    result = execute.fetchall()
    actors_list = []
    for cast in result:
        actors_list.extend(cast[0].split(', '))
    result_list = []
    counter = Counter(actors_list)
    for actor, count in counter.items():
        if actor not in [actor1, actor2] and count > 2:
            result_list.append(actor)
    return result_list


def content_by_parameters(content_type, release_year, genre):
    """Подбор контента по типу, году и жанру"""
    query = f"""
            SELECT title, description
            FROM netflix
            WHERE type LIKE '%{content_type}%'
            AND release_year LIKE '%{release_year}%'
            AND listed_in LIKE '%{genre}%'
            """
    execute = execute_query(query, DB_PATH)
    result = execute.fetchall()
    result_list = []
    for content in result:
        result_list.append({
            "title": content[0],
            "description": content[1]
        })
    return result_list
