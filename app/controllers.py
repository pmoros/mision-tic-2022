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
        # try:
        #     db.session.add(product)
        #     db.session.commit()
        # except Exception as e:
        #     db.session.rollback()
        #     product = Product.query.filter_by(id=product.id).first()
        pass

    def get_all_products(self):
        # return Product.query.all()
        dummy_products = [Product(id=1, name="Product 1", description="Handy product 1", price=10.0, image="https://via.placeholder.com/150", stock=10),
                          Product(id=2, name="Product 2", description="Handy product 2", price=20.0,
                                  image="https://via.placeholder.com/150", stock=20), Product(id=3, name="Product 3", description="Handy product 3", price=30.0, image="https://via.placeholder.com/150", stock=30), Product(id=4, name="Product 4", description="Handy product 4", price=40.0, image="https://via.placeholder.com/150", stock=0)]

        return dummy_products

    def get_product(self, product_id):
        # return Product.query.get(product_id)
        pass

    def get_products_ordered_by(self, field, asc=True):
        # if asc:
        #     return Product.query.order_by(Product.name).all()
        # else:
        #     return Product.query.order_by(Product.name.desc()).all()

        pass


user_controller = UserController()
product_controller = ProductController()
