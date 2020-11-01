from db import Users, db


class UserModel():

    __tablename__ = 'users'

    def __init__(self, _user_uuid=None, user_email=None, user_password=None, first_name=None, last_name=None):
        self.user_uuid = _user_uuid
        self.user_email = user_email
        self.user_password = user_password
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = True

    def json(self, user_email, first_name, last_name):
        return {
            'user_email': user_email,
            'first_name': first_name,
            'last_name': last_name
        }

    def find_by_user_email(self, user_email):
        return db.session.query(Users).filter_by(user_email=user_email).first()

    def find_by_user_uuid(self, _user_uuid):
        return db.session.query(Users).filter_by(user_uuid=_user_uuid).first()

    def save_to_db(self):
        new_user = Users(
            user_uuid=self.user_uuid,
            user_email=self.user_email,
            user_password=self.user_password,
            first_name=self.first_name,
            last_name=self.last_name,
            is_active=self.is_active
        )
        db.session.add(new_user)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
