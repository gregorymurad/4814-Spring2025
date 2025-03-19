from flask import Flask
import os


app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def index():
    return "<h1>Hello, COP 4814 students!</h1>"


if __name__ == '__main__':
    app.run(debug=True)