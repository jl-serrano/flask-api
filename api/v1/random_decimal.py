from flask_restful import Resource
import random

class RandomDecimal(Resource):
    def get(self):
        return round(random.random(), 2)

