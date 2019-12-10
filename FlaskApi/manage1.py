from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Toto je index"

@app.route("/pozdrav/<string:name>")
def hello(name):
	return "Ahoj {}, jak se máš?".format(name)
	# TODO: Pozdravte uživatele podle zadaného jména v proměnné "name"

@app.route("/opava")
def opava():
	return "<h1>Ahoj Opavo!</h1><p>Maliny na tebe</p>"

# TODO: Vytvořte novou routu - například /sekce/<nazev-sekce>. Pro výstup použijte html 

if __name__ == "__main__":
	app.run()
