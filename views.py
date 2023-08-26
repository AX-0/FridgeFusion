from flask import Blueprint, render_template, request, url_for, redirect
from flask import Flask
import markdown
from chat import Chat 

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
    return render_template("RecipeDetails.html")

@app.route('/recipe', methods = ['POST', 'GET'])
def recipe():
    if request.method == "POST":
        ingredients = request.form.get("ingredients")
        dietary = request.form.getlist("dietary")
        allergies = request.form.getlist("allergies")
        if len(dietary) == 0:
            dietary = ["No Dietary Requirements"]
        elif len(allergies) == 0:
            allergies = ["There is no allergy requirement"]
        gpt = Chat(ingredients, dietary, allergies)
        prompt = gpt.prompt_creation()
        gpt.ask_gpt(prompt)
        markdown_text = ""
        with open("test.md", 'r') as f:
            markdown_text = f.read()
        html_content = markdown.markdown(markdown_text)

    return render_template("Recipe.html", markdown_content=html_content)


