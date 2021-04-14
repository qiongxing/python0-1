from flask_restful import Resource, Api
from flask import jsonify

from app import app

# 通过路由直接访问


@app.route('/')
def hello():
    return jsonify({'text': 'Hello World!'})


api = Api(app)

# 通过类访问


class User(Resource):
    def get(self):
        return {'username': 'sherock'}


api.add_resource(User, '/user')
