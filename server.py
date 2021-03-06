import sqlite3
from flask import Flask, render_template, g, jsonify
from flask.ext.cache import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
DATABASE = 'database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        db.close()


@app.route("/")
def root():
    return app.send_static_file('index.html')


@app.route("/data.json")
@cache.cached(timeout=300)
def data():
    cur = get_db().cursor()
    cur.execute('SELECT time, pvp, pve FROM series')
    return jsonify(series = cur.fetchall())


if __name__ == "__main__":
    app.run(debug = True)
