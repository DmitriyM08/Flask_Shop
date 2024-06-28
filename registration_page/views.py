import flask
from .models import User
from shop.settings import DATABASE

def render():
    # Перевіряє, чи метод запиту POST
    if flask.request.method == 'POST':
        # Виводить дані з форми у консоль (для відладки)
        print(flask.request.form)
        
        # Створює новий об'єкт User з даними з форми
        user = User(
            login = flask.request.form['login'],
            email = flask.request.form['email'],
            password = flask.request.form['password'],
            password_confirmation = flask.request.form['password_confirmation'],
            is_admin = flask.request.form['is_admin']
        )
        
        try:
            # Перевіряє, чи пароль і підтвердження пароля збігаються
            if user.password == user.password_confirmation:
                # Додає нового користувача у сесію бази даних
                DATABASE.session.add(user)
                # Зберігає (коммітить) зміни в базу даних
                DATABASE.session.commit()
            else:
                # Повертає повідомлення про помилку, якщо паролі не збігаються
                return 'ERROR'
        except:
            # Повертає повідомлення про помилку у випадку виключення
            return 'ERROR'
    
    # Якщо метод запиту не POST, рендерить шаблон реєстрації
    return flask.render_template(template_name_or_list="registration.html")
