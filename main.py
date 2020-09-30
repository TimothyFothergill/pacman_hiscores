import pacman_database
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
database = pacman_database


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/api/")
def scores_api():
    data = database.show_all_database_documents()
    return {
        "Scores": {
            "Test": "data1"
            }
    }


@app.route("/submit", methods=["GET", "POST"])
def submit_page():
    return render_template("submit.html")


# username, score, email, image

@app.route("/received", methods=["POST"])
def score_received():
    if request.method == "POST":
        username = request.form["username"]
        score = request.form["score"]
        email = request.form["email"]
        image = request.form["image"]
        if int(score) > 3333360:
            # Built in Flask function Flash may be appropriate, if the user tries to enter something invalid.
            return redirect("/submit")
        save_image(image)
    database.add_to_database(username, score, email, image)
    return "Score received"


@app.route("/list", methods=["GET"])
def list_scores():
    pass


@app.route("/about")
def about_page():
    return render_template("about.html")


def save_image(image):
    pass


app.run(host="0.0.0.0", debug=True)
