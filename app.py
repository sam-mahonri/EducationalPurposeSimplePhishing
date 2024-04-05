from flask import Flask, render_template, request, redirect # importa a classe do Flask da biblioteca flask
from forms import Login

app = Flask("Moretti")
app.config["SECRET_KEY"] = "QualquerCoisa"

@app.route('/')
def home():
    return render_template('index.html', variavel="Henricco bobão")

@app.route('/login', methods=["POST", "GET"])
def sobre():
    form = Login()
    
    if request.method == "POST":
        if form.validate_on_submit():
            print(form.data)
            return redirect("https://kahoot.com")
            
            
    return render_template('login.html', form = form)


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
    