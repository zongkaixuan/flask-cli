# -*- encoding: utf-8 -*-
from app.marshalling import ma
from app.models import Users


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users


user_schema = UserSchema(many=True)
