import hashlib
import threading
import logging

from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import redirect
import sqlite3
import pickle

import transaction
import blockchain

logging.basicConfig(level=logging.DEBUG)
blockchain_obj = blockchain.BlockChain()

app = Flask(__name__)

salt = b"12321"

@app.route("/")
def route_page():
    return redirect("/signup")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    message = {}
    if request.method == "POST":
        email = request.values["mail"]
        password = request.values["pass"]
        hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
        conn = sqlite3.connect("account.db")
        curs = conn.cursor()
        curs.execute("create table if not exists accounts(id integer primary key autoincrement,"
                     " email String, login_password String)")

        conn.commit()
        curs.execute(f"select * from accounts where email = '{email}'")
        if curs.fetchall():
            message = {"msg": "already registered address"}
            curs.close()
            conn.close()
            return render_template("signup.html", message=message)
        else:
            curs.execute(f"insert into accounts(email, login_password) "
                         f"values('{email}', '{hashed_password}')")
            conn.commit()
            curs.execute(f"select id from accounts where email = '{email}'")
            id = curs.fetchone()[0]
            curs.close()
            conn.close()
            return redirect(f"/home/{id}")

    return render_template("signup.html", message=message)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.values["mail"]
        password = request.values["pass"]
        hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
        conn = sqlite3.connect("account.db")
        curs = conn.cursor()
        curs.execute(f"select login_password from accounts where email = '{email}'")
        if hashed_password == curs.fetchone()[0]:
            curs.execute(f"select id from accounts where email = '{email}'")
            id = curs.fetchone()[0]
            curs.close()
            conn.close()
            return redirect(f"/home/{id}")
        curs.close()
        conn.close()
    return render_template("login.html")

@app.route("/home/<id>", methods=["GET", "POST"])
def home(id):
    conn = sqlite3.connect("account.db")
    curs = conn.cursor()
    curs.execute(f"select email from accounts where id = {id}")
    email = curs.fetchone()[0]
    curs.close()
    conn.close()
    value = blockchain_obj.total_value(email)
    message = {"value": value,
           "id": id,
           "name": email}
    if request.method == "POST" and request.values["value"].isdigit():
        sender_address = email
        recipient_address = request.values["to"]
        send_value = int(request.values["value"])
        from_account = transaction.Account(sender_address)
        t = transaction.Transaction(from_account.private_key, from_account.public_key,
                                    sender_address, recipient_address, send_value)
        blockchain_obj.add_transaction(sender_address, recipient_address,
                                       send_value, from_account.public_key, t.generate_signature())
    else:
        message["msg"] = "incorrect!"
    return render_template("home.html", message=message)



def main():
    app.debug = True
    app.run(host="127.0.0.1", port=9999)
    print("hello")

if __name__ == '__main__':
    t1 = threading.Thread(target=blockchain_obj.mining)
    t1.start()
    main()
