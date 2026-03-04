"""
Flask: A minimal web application
"""

from flask import Flask,redirect, url_for, request

app = Flask(__name__)

postcodes = {
        "4021": "Stavanger",
        "0136": "Oslo"
    }

@app.route("/")
def index():
    #return redirect(url_for("static", filename="index.html"))
    return app.send_static_file("index.html")

@app.route("/postcode/<code>")
def citybycode(code):
    if code in postcodes:
        return "Postcode: {} is for {}".format(code, postcodes[code])
    else:
        return "No entry found for postcode {}".format(code),404

@app.route("/lookup")
def lookup():
    pc = request.args.get("postcode","")
    if pc != "":
        return redirect(url_for("citybycode", code=pc))
    else:
        return redirect(url_for("index"))            

@app.route("/postcode", methods=["POST"])
def add():
    pc = request.form.get("postcode", "")
    city = request.form.get("city", "")
    if pc != "" and city != "":
        postcodes[pc] = city
        return redirect(url_for("citybycode", code=pc))
    else:
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()
