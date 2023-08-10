#!/usr/bin/python3
"""Flask Server #1"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/newflask")
def index():
    return render_template("newflask_template.html")

if __name__ == "__main__":
    app.run("0.0.0.0", 8000)

