from flask import Flask, make_response
from flask_restful import Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)

class OKResponse(Resource):
    def get(self):
        response = make_response()
        response.status_code = 200
        return response

class HelloWorld(Resource):
    def get(self):
        return "Hello World" + " - " + datetime.now().strftime("%Y-%m-%d")

api.add_resource(OKResponse, '/')
api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(host='0.0.0.0')