import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

def drop_user_table(conn):
    """Drop table if exists."""
    cur = conn.cursor()
    try:
        sql = "DROP TABLE IF EXISTS users;"
        cur.execute(sql)
        conn.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    else:
        print("Table dropped.")
    finally:
        cur.close()

def create_user_table(conn):
    """Create table."""
    cur = conn.cursor()
    try:
        sql = ("CREATE TABLE users ("
               "userid INTEGER AUTO_INCREMENT, "
               "username VARCHAR(255) NOT NULL UNIQUE, "
               "role ENUM('user', 'admin') NOT NULL, "
               "passwordhash VARCHAR(255) NOT NULL, "
               "PRIMARY KEY(userid))")
        cur.execute(sql)
        conn.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    else:
        print("Table created.")
    finally:
        cur.close()

def add_user(conn, username, hash, role="user"):
    """Add user. Returns the new user id"""
    cur = conn.cursor()
    try:
        sql = ("INSERT INTO users (username, passwordhash, role) VALUES (%s,%s, %s)")
        cur.execute(sql, (username, hash, role))
        conn.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return -1
    else:
        print("User {} created with id {}.".format(username, cur.lastrowid))
        return cur.lastrowid
    finally:
        cur.close()

def get_user_by_name(conn, username):
    """Get user details by name."""
    cur = conn.cursor()
    try:
        sql = ("SELECT userid, username, role FROM users WHERE username = %s")
        cur.execute(sql, (username,))
        for row in cur:
            (id,name, role) = row
            return {
                "username": name,
                "userid": id,
                "role": role
            }
        else:
            #user does not exist
            return {
                "username": username,
                "userid": None,
                "role" : None
            }
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        cur.close()

def get_hash_for_login(conn, username):
    """Get user details from id."""
    cur = conn.cursor()
    try:
        sql = ("SELECT passwordhash FROM users WHERE username=%s")
        cur.execute(sql, (username,))
        for row in cur:
            (passhash,) = row
            return passhash
        else:
            return None
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        cur.close()


if __name__ == "__main__":
    
    pw = input("Enter password for MySQL root user: ")  
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=pw,
            database="dat130"
        )
    except mysql.connector.Error as err:
        print(err)
    else:
        drop_user_table(conn)
        create_user_table(conn)
        add_user(conn,"johndoe", generate_password_hash("Joe123"), "admin")
        add_user(conn,"maryjane", generate_password_hash("LoveDogs"), "admin")
        hash = get_hash_for_login(conn, "maryjane")
        print("Check password: {}".format(check_password_hash(hash,"LoveDogs")))
        
        conn.close()
