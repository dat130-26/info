"""
Flask: Using MySQL
"""

from flask import Flask, render_template, g, request, flash, redirect, url_for

from database import (
    add_postcode,
    connect_db,
    delete_postcode,
    init_postcodes,
    list_postcodes,
    lookup_location,
)

app = Flask(__name__)

# Application config
app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "foobarfoo"
app.config["DATABASE_DB"] = "dat130"
app.config["DATABASE_HOST"] = "localhost"
app.debug = True  # only for development!
app.secret_key = 'some_secret'  # needed for flashing

def get_db():
    if not hasattr(g, "_database"):
        print("create connection")
        g._database = connect_db(
            host=app.config["DATABASE_HOST"],
            user=app.config["DATABASE_USER"],
            password=app.config["DATABASE_PASSWORD"],
            database=app.config["DATABASE_DB"],
        )
    return g._database


@app.teardown_appcontext
def teardown_db(error):
    """Closes the database at the end of the request."""
    db = getattr(g, '_database', None)
    if db is not None:
        print("close connection")
        db.close()


@app.route("/init")
def init():
    """Creates a table and initializes it with some data."""
    postcodes = {
        "0001": "Oslo",
        "4036": "Stavanger",
        "4041": "Hafrsfjord",
        "7491": "Trondheim",
        "9019": "Tromsø"
    }
    db = get_db()
    try:
        init_postcodes(db, postcodes)
        flash("Successful initialization")
    except Exception as err:
        return render_template("error.html", msg=err)

    return redirect(url_for("index"))


@app.route("/listall")
def list_all():
    """Lists all postcodes."""
    db = get_db()
    try:
        postcodes = list_postcodes(db)
        return render_template("listing.html", postcodes=postcodes)
    except Exception:
        return render_template("error.html", msg="Error querying data")


@app.route("/add")
def add():
    """Displays add postcode form."""
    return render_template("add.html")


@app.route("/do_add", methods=["POST"])
def do_add():
    """Adds new postcode to database."""
    postcode = request.form.get("postcode", "")
    location = request.form.get("location", "")
    if postcode and location:
        db = get_db()
        try:
            add_postcode(db, postcode, location)
            flash("Postcode added")
        except Exception:
            return render_template("error.html", msg="Error adding postcode. (Does it exist already?)")
        return redirect(url_for("add"))
    else:
        return render_template("error.html", msg="Input error")


@app.route("/delete/<postcode>")
def delete(postcode):
    """Deletes a given postcode."""
    db = get_db()
    try:
        delete_postcode(db, postcode)
        return redirect(url_for("list_all"))
    except Exception:
        return render_template("error.html", msg="Error deleting data")


@app.route("/lookup")
def lookup():
    """Looks up a given postcode."""
    location = None
    postcode = request.args.get("postcode")
    if postcode:
        db = get_db()
        try:
            location = lookup_location(db, postcode)
        except Exception:
            return render_template("error.html", msg="Error during search")
    return render_template("lookup.html", postcode=postcode, location=location)


@app.route("/")
def index():
    """Displays index page."""
    return render_template("index.html")


if __name__ == "__main__":
    password = input("Please enter the root password for your mysql server:")
    app.config["DATABASE_PASSWORD"] = password
    
    app.run()
