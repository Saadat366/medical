from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/drugs")
def drugs():
    druglist = [
        "paracetamol",
        "linkus",
        "antigrippin",
        "cavinton",
        "canephron"
    ]
    return render_template("drugs.html", druglist=druglist)

@app.route("/recommendations")
@app.route("/recommendations/<string:man>")
def recomendations(man=""):
    return render_template("recomendations.html", man=man)
