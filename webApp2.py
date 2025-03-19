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
    return render_template("aboutUs.html")

if __name__ == '__main__':
    app.run(debug=True, port=8080)