from flask import Blueprint, render_template
from flask import Flask
import chat 

app = Flask(__name__)

# views = Blueprint(__name__, "views")

@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("HomePage.html")

@app.route('/recipe', methods = ['POST', 'GET'])
def recipe():
    return render_template("inputIngredient.html")
