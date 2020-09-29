import pymongo
from flask import Flask, redirect, render_template
app = Flask(__name__)
client = pymongo.MongoClient()
db = client["hiscores"]
col = db["latest"]


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/api/")
def scores_api():
    return "We\'re here"


@app.route("/submit")
def submit_page():
    return render_template("submit.html")


@app.route("/about")
def about_page():
    return render_template("about.html")


app.run(host="0.0.0.0", debug=True)
