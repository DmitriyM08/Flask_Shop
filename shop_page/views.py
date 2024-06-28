import flask
import flask_login
import registration_page
import registration_page.models

def show_shop_page():
    # Отримує всіх користувачів з таблиці User
    user = registration_page.models.User.query.all()
    
    # Логінить кожного користувача (ймовірно, тут є логічна помилка, оскільки повинно логінити лише поточного користувача)
    for users in user:
        flask_login.login_user(users)
    
    # Перевіряє, чи поточний користувач аутентифікований
    if not flask_login.current_user.is_authenticated:
        # Якщо ні, рендерить шаблон shop.html
        return flask.render_template(template_name_or_list="shop.html")
    else:
        # Якщо користувач аутентифікований
        if flask_login.current_user.is_authenticated:
            # Встановлює змінні для шаблону
            name = True
            name2 = users.login
            is_admin = flask_login.current_user.is_admin
            # Рендерить шаблон shop.html з додатковими змінними
            return flask.render_template(template_name_or_list="shop.html", name = name, name2 = name2, is_admin = is_admin)
