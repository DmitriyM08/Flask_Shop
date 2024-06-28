import flask
import flask_login
import registration_page
import registration_page.models
from shop.settings import DATABASE
from .models import Cart

def show_cart_page():
    # Перевіряє, чи метод запиту POST
    if flask.request.method == "POST":
        # Створює новий об'єкт Cart з даними з форми
        cart = Cart(
            name = flask.request.form['name'],
            surname = flask.request.form['surname'],
            phone = flask.request.form['phone'],
            email = flask.request.form['email'],
            city = flask.request.form['city'],
            nova_poshta = flask.request.form['mail'],
            wishes = flask.request.form['wishes']
        )

        # Додає новий об'єкт cart у сесію бази даних
        DATABASE.session.add(cart)
        # Зберігає (коммітить) зміни в базу даних
        DATABASE.session.commit()
    
    # Отримує всіх користувачів з таблиці User
    user = registration_page.models.User.query.all()
    for users in user:
        # Логінить кожного користувача
        flask_login.login_user(users)
    
    # Перевіряє, чи поточний користувач аутентифікований
    if not flask_login.current_user.is_authenticated:
        # Якщо ні, рендерить шаблон cart.html
        return flask.render_template(template_name_or_list="cart.html")
    else:
        if flask_login.current_user.is_authenticated:
            # Встановлює змінні для шаблону
            name = True
            name2 = users.login
            is_admin = flask_login.current_user.is_admin
            # Рендерить шаблон cart.html з додатковими змінними
            return flask.render_template(template_name_or_list="cart.html", name=name, name2=name2, is_admin=is_admin)
