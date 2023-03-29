import sqlite3
from db import db

class BlogModel(db.Model) :

    __tablename__ = "blogs"
    id      = db.Column(db.Integer , primary_key = True)
    title    =  db.Column(db.String(80))
    content    =  db.Column(db.String(80))

    # create a relationship with user, a blog or many blogs are attached to a user
    user_id= db.Column(db.Integer , db.ForeignKey('users.id'))
    store   = db.relationship('UserModel')

    def __init__(self, title , content , user_id):
        self.title     = title
        self.content   = content
        self.user_id   = user_id

    def json(self):
        return {'title' : self.title , 'content' : self.content, 'user_id':  self.user_id}

    @classmethod
    def find_blog_by_id(cls,id):
        return cls.query.filter_by(id = id).first()


    def save_to_db(self):
        """this method serves to update insert blogs
        """
        db.session.add(self) #if the id already exists it makes an update else it add a new element to the db
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls):
        return cls.query.all()

