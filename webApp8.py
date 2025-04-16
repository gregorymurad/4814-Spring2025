from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators
import os
from wtforms.validators import NumberRange
import main_functions
import requests

""" Example of Flask Web App with the News API """
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

def get_key(filename,api_name):
    api_key_dict = main_functions.read_from_file(filename)
    my_api_key = api_key_dict[api_name]
    return my_api_key

news_api_key = get_key("apiKeys/news_apis.json","apiKey")

def get_list_news(category,keyword,news_api_key):
    url=f"https://newsapi.org/v2/top-headlines?category={category}&q={keyword}&apiKey={news_api_key}"
    response = requests.get(url).json()
    # process the response to show just the title, summary, link
    return response

class SearchNews(FlaskForm):
    category = SelectField("Choose a Topic",
                         choices=[
                                    ("business","Business"),
                                    ("entertainment","Entertainment"),
                                    ("general","General"),
                                    ("health","Health"),
                                    ("science","Science"),
                                    ("sports","Sports"),
                                    ("technology","Technology")
                         ])
    keyword = StringField("Keyword")
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form =  SearchNews(request.form)
    if request.method=="POST":
        category = form.category.data # or request.form["camera"]
        keyword = form.keyword.data # or request.form["sol"]
        list_of_articles = get_list_news(category,keyword,news_api_key)
        return render_template("displayNews.html",list_of_articles=list_of_articles)
    else:
        return render_template('searchNews.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)