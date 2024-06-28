import flask
from shop_page.models import Product
from shop.settings import DATABASE

def show_admin_page():
    if flask.request.method == 'POST':
        product = Product(
            name = flask.request.form['name'],
            price = flask.request.form['price'],
            discount = flask.request.form['discount'],
            discount_price = flask.request.form['discount_price']
        )

        DATABASE.session.add(product)
        DATABASE.session.commit()
    return flask.render_template(template_name_or_list="admin.html")