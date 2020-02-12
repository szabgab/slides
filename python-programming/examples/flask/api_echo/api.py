from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class Echo(Resource):
    def get(self):
        return { "prompt": "Type in something" }
    def post(self):
        return { "echo": "This" }

api.add_resource(Echo, '/echo')

