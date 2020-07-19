from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/database")
def database():
    return render_template("database.html")

@app.route("/sources")
def sources():
    return render_template("sources.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    print("server is running")
    app.run(debug=True)