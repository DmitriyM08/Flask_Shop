from .settings import shop_app
from flask_mail import Mail, Message

shop_app.config['MAIL_SERVER'] = 'tkachbogdan12.pythonanywhere.com'
shop_app.config['MAIL_PORT'] = 587
shop_app.config['MAIL_USE_TLS'] = True
shop_app.config['MAIL_USERNAME'] = 'rudy.bodik@gmail.com'
shop_app.config['MAIL_PASSWORD'] = 'tkach12bogdan'