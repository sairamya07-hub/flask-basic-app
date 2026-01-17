from flask import Flask, render_template, request
from database import insert_user, get_all_users


app = Flask(__name__)

@app.route("/")
def home():
    name = "Sai"
    return render_template("index.html", name=name)

@app.route("/about")
def about():
    return "Hi, I am learning Flask and building backend projects."
@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form["name"]
        insert_user(name)
        return render_template("greet.html", name=name)
    return render_template("greet.html")

@app.route("/users")
def users():
    users = get_all_users()
    return render_template("users.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)
