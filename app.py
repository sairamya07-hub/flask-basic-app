from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Sai"
    return render_template("index.html", name=name)

@app.route("/about")
def about():
    return "Hi, I am learning Flask and building backend projects."

if __name__ == "__main__":
    app.run(debug=True)
