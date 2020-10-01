import pacman_database
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
database = pacman_database


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/api/")
def scores_api():
    usernames = []
    scores = []
    emails = []
    images = []
    for document in database.col.find():
        usernames.append(document.get("username"))
        scores.append(document.get("score"))
        emails.append(document.get("email"))
        images.append(document.get("image"))
    return {
        "data": {
            "username": usernames,
            "scores": scores,
            "emails": emails,
            "images": images
        }
    }


@app.route("/submit", methods=["GET"])
def submit_page():
    return render_template("submit.html")


@app.route("/received", methods=["POST"])
def score_received():
    if request.method == "POST":
        username = request.form["username"]
        score = request.form["score"]
        email = request.form["email"]
        image = request.form["image"]
        if int(score) > 3333360:
            # Flask Flash may be appropriate, if the user tries to provide something invalid. HTML5 does enough for now.
            return redirect("/submit")
        save_image(image)
    database.add_to_database(username, score, email, image)
    return render_template("received.html")


@app.route("/list", methods=["GET"])
def list_scores():
    usernames = []
    scores = []
    emails = []
    images = []
    for document in database.col.find():
        usernames.append(document.get("username"))
        scores.append(document.get("score"))
        emails.append(document.get("email"))
        images.append(document.get("image"))
    record = [usernames, scores, emails, images]
    return render_template("list.html", list=record)


@app.route("/about")
def about_page():
    return render_template("about.html")


def save_image(image):
    pass


app.run(host="0.0.0.0", debug=True)
