from flask import Flask, render_template
import random

app = Flask(__name__)

affirmations = [
    "You are capable of amazing things.",
    "You are doing your best, and that is enough.",
    "You are growing and learning every day.",
    "You deserve success and happiness.",
    "You are stronger than you think."
]

@app.route("/")
def home():
    affirmation = random.choice(affirmations)
    return render_template("index.html", affirmation=affirmation)

@app.route("/all")
def all_affirmations():
    return render_template("affirmations.html", affirmations=affirmations)

if __name__ == "__main__":
    app.run()
