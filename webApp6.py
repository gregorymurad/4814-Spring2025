from flask import Flask, render_template, request
import os
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, RadioField, SelectField, SubmitField


app = Flask(__name__)
app.secret_key = os.urandom(16)

class SignUp(FlaskForm):
    first_name = StringField("Enter your first name:")
    last_name = StringField("Enter your last name:")
    email = EmailField("Enter your email address:", description="FIU Email Address")
    pid = IntegerField("Enter your PantherID:")
    campus = RadioField("Campus:", choices=[
        ("mmc","Modesto A. Maidique Campus"),
        ("bbc","Biscayne Bay Campus"),
        ("dc","FIU in DC"),
        ("ec","Engineering Center")
    ])
    major = SelectField("Major", choices=[
        ("ds","Data Science and AI"),
        ("it","Information Technology"),
        ("cys","CyberSecurity"),
        ("cs","Computer Science")
    ])
    submit = SubmitField("Submit")

@app.route('/', methods=["GET","POST"])
def index():
    # create the form
    form = SignUp(request.form)
    if request.method == "POST":
        pass
    else:
        return render_template("signup.html",form=form)

if __name__ == '__main__':
    app.run(debug=True)