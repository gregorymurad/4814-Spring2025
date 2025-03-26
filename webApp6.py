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
        response_dict = {
            "firstName":request.form["first_name"],
            "lastName":request.form["last_name"],
            "email":request.form["email"],
            "pantherid":request.form["pid"],
            "campus":request.form["campus"],
            "major":request.form["major"]
        }
        # Other ways to save user's input:
        # - save to variables
        # - put in a list
        # - save it to a csv file
        # - save it to a json file
        # - send it to a database (safest!)
        return render_template("success.html",
                               name=response_dict["firstName"])
    else:
        return render_template("signup.html",form=form)

if __name__ == '__main__':
    app.run(debug=True)