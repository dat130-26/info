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

def add_user(conn, username, hash):
    """Add user. Returns the new user id"""
    pass

def get_user_by_name(conn, username):
    """Get user details by name. Return id and username."""
    pass
    

def get_hash_for_login(conn, username):
    """Get password hash for user."""
    return None


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
        add_user(conn,"johndoe", generate_password_hash("Joe123"))
        add_user(conn,"maryjane", generate_password_hash("LoveDogs"))
        hash = get_hash_for_login(conn, "maryjane")
        if hash:
            print("Check password: {}".format(check_password_hash(hash,"LoveDogs")))
        
        conn.close()
