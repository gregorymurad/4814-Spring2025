from flask import Flask, render_template
import os


app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def index():
    first_name = "Greg"
    last_name = "Reis"
    return f"<h2>Hello, {first_name} {last_name}!</h2>"

@app.route('/aboutUs')
def aboutUs():
    from datetime import date
    today = date.today()
    # print(today)
    return render_template("aboutUs.html",dt=today)

@app.route('/courses')
def courses():
    my_courses = ["COP4814", "CAP4104", "CAP2752", "CAP2757", "CIS7910"]
    return render_template("courses.html",mc=my_courses)

if __name__ == '__main__':
    app.run(debug=True, port=8080)