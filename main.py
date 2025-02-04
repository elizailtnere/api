from flask import Flask, render_template, request, jsonify
import requests
import random

app = Flask(__name__)

banned_lieotaji = []

chat_background: "white"

@app.route('/', methods=["POST", "GET"])
def index():
    meklet_vardu = None
    jokes = []  

    if request.method == 'POST':
        meklet_vardu = request.form.get('meklet')  

    if meklet_vardu: 
        for _ in range(10):
            atbilde = requests.get("https://api.chucknorris.io/jokes/random")
            joks = atbilde.json()
            if meklet_vardu.lower() in joks["value"].lower():  
                jokes.append(joks)
                break
        if not jokes:  
            jokes = [requests.get("https://api.chucknorris.io/jokes/random").json()]  
    else:
        atbilde = requests.get("https://api.chucknorris.io/jokes/random")
        joks = atbilde.json()
        jokes = [joks]


    return render_template('index.html', jokes=jokes)


@app.route("/uni")
def uni():
    atbilde = requests.get("http://universities.hipolabs.com/search?country=latvia")
    visas = atbilde.json()
    nosaukumi = []
    for elements in visas:
        pieliekamais = {
            "nosaukums": elements["name"],
            "majaslapas": elements["web_pages"]
        }
        nosaukumi.append(pieliekamais)

    return render_template("universitates.html", uni=nosaukumi)


@app.route("/jschats")
def chats():
    return render_template("chats.html")


@app.route("/jschats/suutiit", methods=["POST"])
def suutiit():
    sanemtais = request.json
    if sanemtais["saturs"] == "\clear":
        with open("chataZinas.txt", "w") as f:
            f.write("") 
        return "Izdzests"
    with open("chataZinas.txt", "a") as f:
        f.write(sanemtais["vards"])
        f.write("----")
        f.write(sanemtais["saturs"])
        f.write('\n')
    return jsonify("OK")


@app.route("/jschats/lasiit")
def lasit():
    saturs = []
    with open("chataZinas.txt", "r") as f:
        saturs = f.readlines()  
    return jsonify(saturs)


if __name__ == '__main__': 
    app.run(port=5000)
