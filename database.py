import sqlite3 as sq

class DataBase():
    def __init__(self):
        pass

    def refresh_users(self):
        with sq.connect("shop3_0.db") as con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS users")
            cur.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                refer_id TEXT
                )""")

    def refresh_softs(self):
        with sq.connect("shop3_0.db") as con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS software")
            cur.execute("""CREATE TABLE IF NOT EXISTS software (
            name TEXT PRIMARY KEY,
            description TEXT,
            price TEXT
            )""")

    def refresh_partners(self):
        with sq.connect("shop3_0.db") as con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS partners")
            cur.execute("""CREATE TABLE IF NOT EXISTS partners (
            user_id TEXT PRIMARY KEY,
            name TEXT,
            promocode TEXT,
            discount INTEGER,
            quantity INTEGER
            )""")


    def adduser(self, user_id, name, message):
        with sq.connect("shop3_0.db") as con:
            cur = con.cursor()
            cur.execute(f"INSERT INTO users VALUES({user_id}, '{name}', '{message.text[7::]}')")

    def addsoft(self, name, desc, price):
        with sq.connect("shop3_0.db") as con:
            cur = con.cursor()
            cur.execute(f"INSERT INTO software VALUES('{name}', '{desc}', {price})")

    def delsoft(self, name):
        with sq.connect("shop3_0.db") as con:
            cur = con.cursor()
            cur.execute(f"DELETE FROM software WHERE name = '{name}'")

    def addpartner(self, user_id, name, promocode, discount, quantity):
        with sq.connect("shop3_0.db") as con:
            cur = con.cursor()
            cur.execute(f"INSERT INTO partners VALUES('{user_id}', '{name}', '{promocode}', {discount}, {quantity})")

    def delpartner(self, user_id):
        with sq.connect("shop3_0.db") as con:
            cur = con.cursor()
            cur.execute(f"DELETE FROM partners WHERE user_id = '{user_id}'")

    def select_software_info(self, name):
        with sq.connect("shop3_0.db") as con:
            cur = con.cursor()
            cur.execute(f"SELECT name, description, price FROM software WHERE name = '{name}'")
            rows = cur.fetchall()
            return rows
