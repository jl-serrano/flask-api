from flask_restful import Api
from app import App
from api.v1.random_decimal import RandomDecimal
from api.v1.users import Users

api = Api(App)

api.add_resource(RandomDecimal, '/api/v1/random/decimal')
api.add_resource(Users, '/api/v1/users/<string:user_id>')
