from flask import Flask, render_template
import random

app = Flask(__name__)

weather = [
    {"name": "Sunny like vanilla ice cream",
     "image": "http://www.bien-etre-au-naturel.fr/wp-content/uploads/2013/06/conseil-observation-soleil.jpg"},
    {"name": "Singing in the rain",
     "image": "https://i.pinimg.com/originals/cd/58/ac/cd58aced94b29a45d3fb6c5a18dafb6b.jpg"},
    {"name": "Cloudy", "image": "http://www.awazin.com/wp-content/uploads/2015/02/forme-nuage-cheval.jpg?x83625"},
    {"name": "Thunder, feel the thunder",
     "image": "https://image.freepik.com/free-icon/thunder-bolt-hand-drawn-shape-outline_318-52074.jpg"}
]


@app.route('/')
def index():
    return render_template('page.html')


@app.route('/me')
def me():
    return render_template('page3.html')


@app.route('/weather')
def meteo():
    day_weather = random.choice(weather)
    return render_template('page2.html', wea1=day_weather)


app.run(debug='True', port='8080')
