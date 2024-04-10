from flask import Flask, render_template, request, redirect # importa a classe do Flask da biblioteca flask
from forms import Login
from config import AppConfig

app = Flask(__name__)
app.config.from_object(AppConfig)

@app.route('/')
def home():
    return render_template('index.html', variavel="Henricco bobão")

@app.route('/login', methods=["POST", "GET"])
def sobre():
    form = Login()
    
    if request.method == "POST":
        if form.validate_on_submit():
            print(form.data)
            return redirect("https://kahoot.it")

    return render_template('login.html', form = form)


def create_app():
    return app
    