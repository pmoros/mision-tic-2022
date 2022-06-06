from sqlalchemy.exc import IntegrityError
from app import app
from app.models import Product, db, User


class UserController():
    def get_user(self, user_info):
        user_sub = user_info["sub"]

        return User.query.filter_by(sub=user_sub).first()

    def create_user(self, user_info):
        user_sub = user_info["sub"]
        user_name = user_info["name"]
        user_email = user_info["email"]
        user_profile_pic = user_info["picture"]
        try:
            user = User(sub=user_sub, name=user_name,
                        email=user_email, profile_pic=user_profile_pic)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            user = User.query.filter_by(sub=user_sub).first()

        return user


class ProductController():
    def create_product(self, product):
        product = Product(name=product.get("name", ""), description=product.get("description", ""), image=product.get("image", ""), price=product.get("price", 0),
                          stock=product.get("stock", 0), available=product.get("available", 0), store_id=product.get("store_id", 1), productLine_id=product.get("productLine_id", 1))
        try:
            db.session.add(product)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            app.logger.error(e)

        return Product.query.order_by(Product.id.desc()).first().id

    def get_all_products(self):
        return Product.query.all()

    def get_product(self, product_id):
        return Product.query.get(product_id)

    def edit_product(self, product_id, product_values):
        product = Product.query.get(product_id)
        product.name = product_values.get("name", product.name)
        product.description = product_values.get(
            "description", product.description)
        product.image = product_values.get("image", product.image)
        product.price = product_values.get("price", product.price)
        product.stock = product_values.get("stock", product.stock)
        product.available = product_values.get("available", product.available)
        product.store_id = product_values.get("store_id", product.store_id)
        product.productLine_id = product_values.get(
            "productLine_id", product.productLine_id)

        db.session.commit()

    def delete_product(self, product_id):
        product = Product.query.get(product_id)
        db.session.delete(product)
        db.session.commit()


user_controller = UserController()
product_controller = ProductController()
