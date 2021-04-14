from orm_conn import db, app
import datetime
# from passlib.apps import custom_app_context as pwd_context
# from itsdangerous import (TimedJSONWebSignatureSerializer
#                           as Serializer, BadSignature, SignatureExpired)


class Users(db.Model):
    """用户表"""
    __tablename__ = "users"
    __table_args__ = {'mysql_engine': "InnoDB"}  # 支持事务操作，外键
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), unique=True, nullable=False)
    user_pass = db.Column(db.String(255), nullable=False)
    user_email = db.Column(db.String(255), nullable=False)
    user_date = db.Column(db.DateTime, default=datetime.datetime.now())
    user_level = db.Column(db.Integer,default = -1)

    def __init__(self, name, psd,email):
        self.user_name = name
        self.user_pass = psd
        self.user_email = email


use2 = Users('test2', 'test','test@qq.com')
db.session.add(use2)
db.session.commit()
