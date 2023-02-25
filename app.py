from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def pic():
    return render_template("szad.html")

if __name__ == "__main__":
    app.run(debug=True)

