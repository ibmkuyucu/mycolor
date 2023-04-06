import os
import socket

from flask import Flask, render_template

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

COLOR_FROM_ENV = os.environ.get('APP_COLOR')


@app.route("/")
def main():
    if COLOR_FROM_ENV in color_codes:
        color = color_codes.get(COLOR_FROM_ENV)
    else:
        color = "#000000"
    return render_template('hello.html', name=socket.gethostname(), color=color)


if __name__ == "__main__":
    app.run(debug=True)
