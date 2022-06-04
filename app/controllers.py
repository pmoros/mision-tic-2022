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


user_controller = UserController()
