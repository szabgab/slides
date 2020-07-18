from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)

api = Api(app)


class Echo(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', help='Type in some text')
        args = parser.parse_args()
        return { "res": f"Text: {args['text']}" }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', help='Type in some text')
        args = parser.parse_args()
        return { "Answer": f"You said: {args['text']}" }


api.add_resource(Echo, '/echo')

