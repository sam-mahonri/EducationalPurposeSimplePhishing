
from flask_limiter.util import get_remote_address

class AppConfig():

    LIMITER_ENABLED = True
    LIMITER_STORAGE_URI = "memory://"
    LIMITER_KEY_FUNC = get_remote_address
    
    FLASK_DEBUG = True # Configura o app para depuração
    FLASK_ENV = "development" # Configura o ambiente para o tipo desenvolvimento
    
    SECRET_KEY = "elonmusk"