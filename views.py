from flask import Blueprint, render_template, request, url_for, redirect, session
from flask import Flask
import markdown
from chat import Chat 

app = Flask(__name__)

# views = Blueprint(__name__, "views")
# ingredients = []
# dietary = []
# allergies = []
app.secret_key = "THIS_IS_BAD"
# session = {}
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
        session['ingredients'] = request.form.get("ingredients")
        session['dietary'] = request.form.getlist("dietary")
        session['allergies'] = request.form.getlist("allergies")
        

        if len(session['dietary']) == 0:
            session['dietary'] = ["No Dietary Requirements"]
        elif len(session['allergies']) == 0:
            session['allergies'] = ["There is no allergy requirement"]
        
        gpt = Chat(session['ingredients'], session['dietary'], session['allergies'])
        prompt = gpt.prompt_creation()
        gpt.ask_gpt(prompt)
        markdown_text = ""
        with open("test.md", 'r') as f:
            markdown_text = f.read()
      
        return render_template(
            "Recipe.html",
            ingredients=session['ingredients'],
            dietary=session['dietary'],
            allergies=session['allergies'],
            markdown_content=markdown.markdown(markdown_text)
        )
    else:
        gpt = Chat(session['ingredients'], session['dietary'], session['allergies'])
        prompt = gpt.prompt_creation()
        gpt.ask_gpt(prompt)
        markdown_text = ""
        with open("test.md", 'r') as f:
            markdown_text = f.read()
        return render_template(
            "Recipe.html",
            ingredients=session['ingredients'],
            dietary=session['dietary'],
            allergies=session['allergies'],
            markdown_content=markdown.markdown(markdown_text)
        )


