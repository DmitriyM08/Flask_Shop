from shop.settings import DATABASE

class Cart(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer(), primary_key = True)
    name = DATABASE.Column(DATABASE.String(20), nullable = False)
    surname = DATABASE.Column(DATABASE.String(20), nullable = False)
    phone = DATABASE.Column(DATABASE.Integer(), nullable = False)
    email = DATABASE.Column(DATABASE.String(255), nullable = False)
    city = DATABASE.Column(DATABASE.String(255), nullable = False)
    nova_poshta = DATABASE.Column(DATABASE.Integer(), nullable = False)
    wishes = DATABASE.Column(DATABASE.String(), nullable = False)

    def __repr__(self) -> str:
        return f"id: {self.id}"