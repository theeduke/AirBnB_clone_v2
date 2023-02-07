#!/usr/bin/python 3
"""
    web application to listen on 0.0.0.0, port 5000
    option "strict_slashes=False"
    routes
        /:display"Hello HBNB"
        /hbnb : display "HBNB"
        /c/<text>: Displays 'C' followed by the value of the <text>
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """displays 'hello HBNB' """
    return("Hello HBNB")

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """dislays 'HBNB' """
    return("HBNB")


@app.route("/C/<text>", strict_slashes=False)
def c(text):
    """Displays 'c' following by the valuue of the text
    text = text.replace("_", " ")
    """
    rturn ("c {}".format(text))


if __name__ == "__main__"
    app.run("host=0.0.0.0", port=5000)
