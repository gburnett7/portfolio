from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/home")
@app.route("/about")
def home():
    return render_template('about.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/timeline")
def timeline():
    return render_template('timeline.html')

@app.route("/photography")
def prhotography():
    return render_template('photography.html')