from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "aubbiedobbieboo"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template("hello.html")