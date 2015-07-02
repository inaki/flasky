from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'algo dificil de adivinar'

from app import views
