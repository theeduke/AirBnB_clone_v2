#!/usr/bin/python3
"""
    web application to listen on 0.0.0.0, port 5000
    option "strict_slashes=False"
    routes
        /:display"Hello HBNB"
        /hbnb : display "HBNB"
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

if__name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
