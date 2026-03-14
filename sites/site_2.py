from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
   return '<h1>Hello</h1> <a href="/random_fact">Посмотреть случайный факт!</a>'

@app.route("/random_fact")
def factes():
    fact_list = ['факт 1', 'факт 2', 'факт 3', 'факт 4', 'факт 5', 'факт 6', 'факт 7']
    return f'<p>{random.choice(fact_list)}</p>'

@app.route("/secret")
def secret():
    return "<h1>Ты нашёл тайную страницу!</h1>"

app.run(debug=True)
