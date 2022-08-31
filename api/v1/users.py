from email import message, parser
from flask_restful import Resource, reqparse
from flask import abort

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help="Name cannot be blank!")
parser.add_argument('age', required=True, help="Age cannot be blank!")
parser.add_argument('gender', required=True, help="Gender cannot be blank!")

users = {
    0: {'name': 'John Doe', 'age': 24, 'gender': 'male'},
    1: {'name': 'Joseph Smith', 'age': 19, 'gender': 'male'},
    2: {'name': 'Jane Ford', 'age': 21, 'gender': 'female'},
    3: {'name': 'Nicole Hayes', 'age': 18, 'gender': 'female'},
}

class Users(Resource):
    def get(self, user_id):
        if user_id == "all":
            return users
        return users[int(user_id)]

    def put(self, user_id):
        user_id = int(user_id)
        args = parser.parse_args()
        new_user = {
            'name': args['name'], 
            'age': args['age'], 
            'gender': args['gender']
        }
        users[user_id] = new_user
        return {user_id: users[user_id]}, 201

    def delete(self, user_id):
        user_id = int(user_id)
        if user_id not in users:
            abort(404, message=f"User {user_id} not found.")
        del users[user_id]
        return { "message": "resource deleted successfully" }, 200