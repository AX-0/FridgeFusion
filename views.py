from flask import Blueprint, render_template, request, url_for, redirect
from flask import Flask
import markdown
import chat 

app = Flask(__name__)

# views = Blueprint(__name__, "views")
ingredients = []
@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("HomePage.html")

@app.route("/home", methods=['POST', 'GET'])
def home2():
    return render_template("HomePage.html")

@app.route('/input', methods = ['POST', 'GET'])
def input():    
    return render_template("InputIngredient.html")

@app.route('/recipe', methods = ['POST', 'GET'])
def recipe():
    if request.method == "POST":
        markdown_text = ""
        with open("test.md", 'r') as f:
            markdown_text = f.read()
        html_content = markdown.markdown(markdown_text)

    return render_template("Recipe.html", markdown_content=html_content)


