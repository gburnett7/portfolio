from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
@app.route("/about")
def home():
    return render_template('about.html')