import os
from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT


from db import db
from security import authenticate,identity
from resources.user import UserRegister
from resources.blog import Blog , ItemList


app             = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]   = os.environ.get('DATABASE_URL')


"""
author: Sabri
Just for testing purposes i hard coded the secret key below, it's better to store it as ENV variable 
"""
app.secret_key  = 'XXX156Ye54'
api             = Api(app)
jwt             = JWT(app,authenticate,identity)



api.add_resource(Blog, '/blog/<int:id>')
api.add_resource(ItemList, '/blogs')

api.add_resource(UserRegister, '/register')


db.init_app(app)

@app.before_first_request
def create_tables():
    ''' this uses all the subclasses of the db.Model to create the tables
    '''
    db.create_all()

if __name__ == '__main__':
    app.run(debug = True)


