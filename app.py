from flask import Flask
from flask import render_template, redirect, request, make_response, jsonify

import os
from services import *

printf = print

#####
api = "/api/v1" 
#####

HOST = "0.0.0.0"
PORT = 5000

DEBUG = True
app = Flask(__name__)

@app.errorhandler(500)
def broken(message):
    return f"500: Internal Server Error\nDebug: {message}"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
    
###########################################################################################

@app.route(f"{api}/random", methods=["GET"])
def random():
    frog = randomcoolfrogimagelol()
    return redirect(frog)
    
@app.route(f"{api}/login", methods=["POST"])
def login():
    if not request.is_json:
        broken("not json lol")
        
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    authenticate, admin = worstauthenticationever(username, password)
    if admin:
        message = f"wooohooo, you admin!!1! {authenticate}"
    else: message = f"logged in as {username}"
    response = make_response(jsonify({"status": message}))
    response.set_cookie("user", authenticate)
    return response

@app.route(f"{api}/win", methods=["GET", "POST"])
def win():
    token = request.cookies.get("user")
    if token:
        winner = didyouwin(token)
        if winner:
            maybe = "YOU WON"
        else: maybe = "NOPEEEEEEE"
    else: broken("no cookie!")
    return make_response(jsonify({"status": maybe}))

###########################################################################################

def main():
    #printf(f"[+] Startng Server ({PORT})")    
    app.run(debug=DEBUG, host=HOST, port=PORT)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        printf(f"Exception: {e}")
