#pip install flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def holaMon():
	return "Hola!"

@app.route("/hello")
def holaMon2():
	return f"Hola DAM!"

@app.route("/hello/<nom>")
def holaMon3(nom):
	return f"Hola {nom}!"

@app.route("/suma/<n1>/<n2>")
def testSuma(n1, n2):
	return f"{int(n1)+int(n2)}"

app.run(port=5000)
