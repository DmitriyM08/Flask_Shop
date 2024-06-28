import flask
import flask_login

import registration_page.models

def show_log_page():
    # Перевіряє, чи метод запиту POST
    if flask.request.method == 'POST':
        # Отримує всіх користувачів з таблиці User
        users = registration_page.models.User.query.all()
        for user in users:
            # Перевіряє, чи введені логін і пароль відповідають записам у базі даних
            if user.login == flask.request.form['login'] and user.password == flask.request.form['password']:
                # Логінить користувача, якщо логін і пароль збігаються
                flask_login.login_user(user)
    
    # Ініціалізує змінну is_admin як False
    is_admin = False

    # Перевіряє, чи поточний користувач аутентифікований
    if not flask_login.current_user.is_authenticated:
        # Якщо користувач не аутентифікований, рендерить шаблон login.html
        return flask.render_template('login.html')
    else:
        # Якщо користувач аутентифікований, встановлює is_admin відповідно до ролі користувача
        is_admin = flask_login.current_user.is_admin
        # Перенаправляє користувача на домашню сторінку
        return flask.redirect('/')
