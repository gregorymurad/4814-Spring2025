from flask import Flask, render_template
import os


app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def index():
    return "<h1> Welcome to my web app </h1>"

@app.route('/coursesInfo')
def coursesInfo():
    courses_info = {
        "COP4814" : ["Component-Based Soft Dev", 50],
        "CAP4104" : ["Human-Computer Interaction", 60],
        "CAP2752" : ["Data Science for All", 60],
        "CAP2757" : ["Intro do Data Science", 22]
    }
    return render_template("coursesInfo.html",coursesInformation = courses_info)

if __name__ == '__main__':
    app.run(debug=True)