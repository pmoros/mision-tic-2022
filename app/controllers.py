from app.models import db, User


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
    def get_all_products(self):
        # return Product.query.all()
        pass

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
