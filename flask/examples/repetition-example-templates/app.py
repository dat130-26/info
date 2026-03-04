"""
Flask: A minimal web application
"""

from flask import Flask,redirect, url_for, request, render_template

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
    return render_template("lookup.html", pc=code, city=postcodes.get(code, ""))

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
    return render_template("add.html", pc=pc, city=city, list=postcodes.items())
    
if __name__ == "__main__":
    app.run(debug=True)
