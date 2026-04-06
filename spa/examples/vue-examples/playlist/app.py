"""
Flask: A minimal web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    songs = [
        {"name": "Test",
         "artist": "tester"},
         {"name": "Best song",
         "artist": "Bester"},
         {"name": "Another song",
         "artist": "Someone else"}
    ]
    return render_template("index.html", playlist = songs)

if __name__ == "__main__":
    app.run()
