"""
Database operations for postcode handling.
"""

import mysql.connector


def connect_db(host, user, password, database):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
    )


def init_postcodes(connection, postcodes):
    cur = connection.cursor()
    try:
        sql = "CREATE TABLE postcodes (postcode VARCHAR(4), location VARCHAR(20), PRIMARY KEY(postcode))"
        cur.execute(sql)
        for postcode, location in postcodes.items():
            sql = "INSERT INTO postcodes (postcode, location) VALUES (%s, %s)"
            cur.execute(sql, (postcode, location))
        connection.commit()
    finally:
        cur.close()


def list_postcodes(connection):
    cur = connection.cursor()
    try:
        postcodes = []
        sql = "SELECT postcode, location FROM postcodes ORDER BY postcode"
        cur.execute(sql)
        for (postcode, location) in cur:
            postcodes.append({
                "postcode": postcode,
                "location": location
            })
        return postcodes
    finally:
        cur.close()


def add_postcode(connection, postcode, location):
    cur = connection.cursor()
    try:
        sql = "INSERT INTO postcodes (postcode, location) VALUES (%s, %s)"
        cur.execute(sql, (postcode, location))
        connection.commit()
    finally:
        cur.close()


def delete_postcode(connection, postcode):
    cur = connection.cursor()
    try:
        sql = "DELETE FROM postcodes WHERE postcode=%s"
        cur.execute(sql, (postcode,))
        connection.commit()
    finally:
        cur.close()


def lookup_location(connection, postcode):
    cur = connection.cursor()
    try:
        sql = "SELECT location FROM postcodes WHERE postcode=%s"
        cur.execute(sql, (postcode,))
        result = cur.fetchone()
        if result is None:
            return None
        (location,) = result
        return location
    finally:
        cur.close()