from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class Echo(Resource):
    def get(self, me):
        return { "res": f"Text: {me}" }

    def post(self, me):
        return { "Answer": f"You said: {me}" }


api.add_resource(Echo, '/echo/<me>')

