import subprocess
import sys

import flask
import DataBase

app = flask.Flask(__name__)


@app.route("/api/parser")
def parsing():
    pages_arg = flask.request.args.get("pages_count")
    args = []

    if pages_arg:
        args += ["-c", pages_arg]

    try:
        subprocess.run([sys.executable, "hw5.py"] + args)
    except Exception:
        return "Unexpected errors occurred!\n", 500

    return "Parsing done.", 200


@app.route("/api/data")
def get_data():
    try:
        psql_client = DataBase.PSQLwriter(
            user="postgres",
            database="products_db",
            table="products"
        )
        json_data = psql_client.write_data_to_json()
    except Exception as error:
        print(f"Ошибка при получении данных: {error}")
        return "Unexpected errors occurred!\n", 500

    return flask.Response(json_data, mimetype='application/json')


@app.route("/api/clear")
def clear():
    try:
        psql_client = DataBase.PSQLwriter(
            user="postgres",
            database="products_db",
            table="products"
        )
        psql_client.clear_table()
    except Exception:
        return "Unexpected errors occurred!\n", 500

    return "Table successfully cleaned.\n", 200


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
