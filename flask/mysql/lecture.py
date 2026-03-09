import mysql.connector
from mysql.connector import errorcode

def createPostcodesTable(conn):
    cur = conn.cursor()
    sql = ("CREATE TABLE postcodes ("
           "postcode VARCHAR(4) UNIQUE, "
           "location VARCHAR(20), "
           "PRIMARY KEY(postcode)"
           ")")
    try:
        cur.execute(sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Error: Table already exists.")
        else:
            print("Error: {}".format(err.msg))
    else:
        print("Table created")
    finally:
        cur.close()
        
def insertPC(conn, pc, loc):
    cur = conn.cursor()
    sql = "INSERT INTO postcodes (postcode, location) VALUES (%s, %s)"
    try:
        cur.execute(sql, (pc,loc))
        conn.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))
    else:
        print("Inserted!")
    finally:
        cur.close()

def insertPCs(conn, pcs):
    cur = conn.cursor()
    sql = "INSERT INTO postcodes (postcode, location) VALUES (%s, %s)"
    try:
        for pc in pcs:
            cur.execute(sql, (pc,pcs[pc]))
        conn.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))
    else:
        print("Inserted!")
    finally:
        cur.close()

def getPC(conn, lower, upper):
    cur= conn.cursor()
    sql = "SELECT postcode, location FROM postcodes WHERE postcode BETWEEN %s AND %s"
    try:
        cur.execute(sql, (lower, upper))
        for (postcode, location) in cur:
            print(postcode, ": ", location)
    except mysql.connector.Error as err:
        print("Error: {}".format(err.msg))
    finally:
        cur.close()

if __name__ == "__main__":
    postcodes = {
        "0001": "Oslo",
        "4036": "Stavanger",
        "4041": "Hafrsfjord",
        "7491": "Trondheim",
        "9019": "Tromsø"
    }
    
    
    try:
        conn = mysql.connector.connect(user='root', password='nikolaus', host='127.0.0.1', database='dat130')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid username/password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(err)
    else:
        print("Did connect")
        createPostcodesTable(conn)
        insertPC(conn, "9019", "Tromsø")
        insertPCs(conn, postcodes)
        getPC(conn, "4000", "8000")
    finally:
        conn.close()