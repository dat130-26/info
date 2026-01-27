"""
Flask: A minimal web application
"""

from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()

print(url_for('index'))
