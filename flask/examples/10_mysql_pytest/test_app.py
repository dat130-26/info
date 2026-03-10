import pytest
import mysql.connector

from app import app as flask_app

# Fixtures are setup functions that are run before a test.
@pytest.fixture
def app():
    flask_app.config["DATABASE_USER"] = "tester"
    flask_app.config["DATABASE_PASSWORD"] = "foobarfoo"
    flask_app.config["DATABASE_DB"] = "test"
    return flask_app

# The client fixture uses the app, so app fixture will be run before.
@pytest.fixture
def client(app):
    return flask_app.test_client()

# A fixture for tests that need an empty database.
@pytest.fixture
def empty_db(app):
    conn = mysql.connector.connect(host=app.config["DATABASE_HOST"], 
                                   user=app.config["DATABASE_USER"], 
                                   password=app.config["DATABASE_PASSWORD"], 
                                   database=app.config["DATABASE_DB"])
    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE IF EXISTS postcodes")
        conn.commit()
    except mysql.connector.Error as err:
        print(err)
    finally:
        cur.close()
        conn.close()

# A fixture for tests that need a database with data.
@pytest.fixture
def db(app, empty_db):
    postcodes = {
        "0001": "Oslo",
        "4036": "Stavanger",
        "4041": "Hafrsfjord",
        "7491": "Trondheim",
        "9019": "Tromsø"
    }

    conn = mysql.connector.connect(host=app.config["DATABASE_HOST"], 
                                   user=app.config["DATABASE_USER"], 
                                   password=app.config["DATABASE_PASSWORD"], 
                                   database=app.config["DATABASE_DB"])
    cur = conn.cursor()
    try:
        sql = "CREATE TABLE IF NOT EXISTS postcodes (postcode VARCHAR(4) UNIQUE, location VARCHAR(20), PRIMARY KEY(postcode))"
        cur.execute(sql)
        for k, v in postcodes.items():
            sql = "INSERT INTO postcodes (postcode, location) VALUES (%s, %s)"
            cur.execute(sql, (k, v))
        conn.commit()  # commit
    except mysql.connector.Error as err:
        print(err)
    finally:
        cur.close()
        conn.close()


def test_index(client):
    """Test that the index page loads."""
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"Index" in rv.data

def test_init(client, empty_db):
    """Test that the init page initializes the database."""
    rv = client.get("/init")
    assert rv.status_code == 302  # redirect to index

def test_list_all(client, db):
    """Test that the list_all page lists all postcodes."""
    rv = client.get("/listall")
    assert rv.status_code == 200
    assert b"0001" in rv.data
    assert b"9019" in rv.data
    
def test_delete_existing(client, db):
    """Test that deleting an existing postcode works."""
    rv = client.get("/delete/0001")
    assert rv.status_code == 302  # redirect to list_all

def test_delete_nonexisting(client, db):
    """Test that deleting a non-existing postcode works."""
    rv = client.get("/delete/9999")
    assert rv.status_code == 404

    
def test_delete_invalid(client, db):
    """Test that deleting with an invalid postcode works."""
    rv = client.get("/delete/abcde")
    assert rv.status_code == 404
    
def test_add_valid(client, db):
    """Test that adding a valid postcode works."""
    rv = client.post("/do_add", data={"postcode": "1234", "location": "Testville"})
    assert rv.status_code == 302  # redirect to list_all

def test_add_existing(client, db):
    """Test that adding a valid postcode works."""
    rv = client.post("/do_add", data={"postcode": "0001", "location": "Oslo"})
    assert rv.status_code == 500

def test_add_invalid(client, db):
    """Test that adding an invalid postcode works."""
    rv = client.post("/do_add", data={"postcode": "abcde", "location": "Testville"})
    assert rv.status_code == 500

def test_add_empty(client, db):
    """Test that adding an empty postcode works."""
    rv = client.post("/do_add", data={"postcode": "", "location": ""})
    assert rv.status_code == 400

def test_add_missing_location(client, db):
    """Test that adding a missing postcode works."""
    rv = client.post("/do_add", data={"postcode": ""})
    assert rv.status_code == 400

def test_add_missing_postcode(client, db):
    """Test that adding a missing postcode works."""
    rv = client.post("/do_add", data={"location": "Testville"})
    assert rv.status_code == 400