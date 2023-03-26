from flask import Flask
from utils import *

app = Flask(__name__)
app.config['ensure_ascii'] = False
app.config['JSON_SORT_KEYS'] = False


@app.route('/movie/<title>')
def get_movie_by_title(title):
    return movie_by_title(title)


if __name__ == "__main__":
    app.run(debug=True, port=1608)
