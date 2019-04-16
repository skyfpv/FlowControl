from flask import Flask
from flask_restful import Api
from controllers import users
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

api.add_resource(users.Users, '/api/v1/users')

if __name__ == '__main__':
    app.run(debug=True)
