"""
Flask: Using MySQL
"""

from flask import Flask, render_template, g, request, flash, redirect, url_for
import mysql.connector

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
        g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"], user=app.config["DATABASE_USER"],
                                       password=app.config["DATABASE_PASSWORD"], database=app.config["DATABASE_DB"])
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
    cur = db.cursor()
    try:
        sql = "CREATE TABLE postcodes (postcode VARCHAR(4) UNIQUE, location VARCHAR(20), PRIMARY KEY(postcode))"
        cur.execute(sql)
        for k, v in postcodes.items():
            sql = "INSERT INTO postcodes (postcode, location) VALUES (%s, %s)"
            cur.execute(sql, (k, v))
        db.commit()  # commit
        flash("Successful initialization")
    except mysql.connector.Error as err:
        return render_template("error.html", msg=err)
    finally:
        cur.close()

    return redirect(url_for("index"))


@app.route("/listall")
def list_all():
    """Lists all postcodes."""
    db = get_db()
    cur = db.cursor()
    try:
        postcodes = []  # holds the data that we will return
        sql = "SELECT postcode, location FROM postcodes ORDER BY postcode"
        cur.execute(sql)
        for (postcode, location) in cur:
            postcodes.append({
                "postcode": postcode,
                "location": location
            })
        return render_template("listing.html", postcodes=postcodes)
    except mysql.connector.Error as err:
        return render_template("error.html", msg="Error querying data"), 500
    finally:
        cur.close()


@app.route("/add")
def add():
    """Displays add postcode form."""
    return render_template("add.html")


@app.route("/do_add", methods=["POST"])
def do_add():
    """Adds new postcode to database."""
    postcode = request.form.get("postcode")
    location = request.form.get("location")
    if postcode and location:
        db = get_db()
        cur = db.cursor()
        try:
            sql = "INSERT INTO postcodes (postcode, location) VALUES (%s, %s)"
            cur.execute(sql, (postcode, location))
            db.commit()
            flash("Postcode added")
        except mysql.connector.Error as err:
            return render_template("error.html", msg="Error adding postcode. (Does it exist already?)"), 500
        finally:
            cur.close()
        return redirect(url_for("add"))
    else:
        return render_template("error.html", msg="Input error"), 400


@app.route("/delete/<postcode>")
def delete(postcode):
    """Deletes a given postcode."""
    db = get_db()
    cur = db.cursor()
    try:
        sql = "DELETE FROM postcodes WHERE postcode=%s"
        cur.execute(sql, (postcode,))  # it's a tuple
        db.commit()
        if cur.rowcount == 0:
            return render_template("error.html", msg="No data to delete"), 404
        return redirect(url_for("list_all"))
    except mysql.connector.Error as err:
        return render_template("error.html", msg="Error deleting data"), 500
    finally:
        cur.close()


@app.route("/lookup")
def lookup():
    """Looks up a given postcode."""
    location = None
    postcode = request.args.get("postcode")
    if postcode:
        db = get_db()
        cur = db.cursor()
        try:
            sql = "SELECT location FROM postcodes WHERE postcode=%s"
            cur.execute(sql, (postcode,))  # it's a tuple
            try:
                (location,) = cur.fetchone()  # the result of fetchone() is also a tuple!
            except:
                pass  # no matching record was found
        except mysql.connector.Error as err:
            return render_template("error.html", msg="Error during search")
        finally:
            cur.close()
    return render_template("lookup.html", postcode=postcode, location=location)


@app.route("/")
def index():
    """Displays index page."""
    return render_template("index.html")


if __name__ == "__main__":
    password = input("Please enter the root password for your mysql server:")
    app.config["DATABASE_PASSWORD"] = password
    app.run()
