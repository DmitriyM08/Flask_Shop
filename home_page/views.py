import flask
import flask_login
from registration_page.models import User

def show_home_page():
    # Отримує всіх користувачів з таблиці User
    user = User.query.all()
    
    # Логінить кожного користувача
    for users in user:
        flask_login.login_user(users)
    
    # Перевіряє, чи поточний користувач аутентифікований
    if not flask_login.current_user.is_authenticated:
        # Якщо ні, рендерить шаблон home.html
        return flask.render_template(template_name_or_list="home.html")
    else:
        # Якщо користувач аутентифікований
        if flask_login.current_user.is_authenticated:
            # Встановлює змінні для шаблону
            name = True
            name2 = users.login
            is_admin = flask_login.current_user.is_admin
            # Рендерить шаблон home.html з додатковими змінними
            return flask.render_template(template_name_or_list="home.html", name = name, name2 = name2, is_admin = is_admin)
