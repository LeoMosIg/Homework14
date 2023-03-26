import sqlite3

from config import DB_PATH


def execute_query(query, path):
    with sqlite3.connect(path) as connection:
        cursor = connection.cursor()
        result = cursor.execute(query)
    return result


def movie_by_title(title):
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
