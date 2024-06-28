from shop.settings import DATABASE

class Product(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer(), primary_key = True)

    name = DATABASE.Column(DATABASE.String(220), nullable = False)
    price = DATABASE.Column(DATABASE.Integer(), nullable = False)
    discount = DATABASE.Column(DATABASE.Integer(), nullable = False)
    discount_price = DATABASE.Column(DATABASE.Integer(), nullable = False)

    def __repr__(self) -> str:
        return f"id: {self.id}"