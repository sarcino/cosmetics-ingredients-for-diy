from flask import Flask, render_template, json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    print("server is running")
    app.run(debug=True)