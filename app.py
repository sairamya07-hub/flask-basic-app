from flask import Flask, render_template, request

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
        return render_template("greet.html", name=name)
    return render_template("greet.html")

if __name__ == "__main__":
    app.run(debug=True)
