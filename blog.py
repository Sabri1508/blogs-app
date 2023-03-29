from flask_restful import Resource,  reqparse
from flask_jwt import  jwt_required

from models.blog import BlogModel


class Blog(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('title',
                        type=str,
                        required=True,
                        help='this field is required')
    parser.add_argument('content',
                        type=str,
                        required=False,
                        help='this field is not required')
    parser.add_argument('_id',
                        type=int,
                        required=True,
                        help='every blog needs a user id')

    @jwt_required()
    def get(self,id):
        """"""
        blog  = BlogModel.find_blog_by_id(id)
        if blog :
            return blog.json()
        return {'message' : f'Blog with {id} not found !'} ,404

    def post(self , id):
        if  BlogModel.find_blog_by_id(id):
            return {'message' : f'blog with {id} already exists'}, 201
        request_data = blog.parser.parse_args()
        blog  = BlogModel(**request_data)
        try :
            blog.save_to_db()
        except :
            return {"message" : "internal error occurred"}, 500
        return blog.json(), 201

    def delete(self,id):
        blog =  BlogModel.find_blog_by_id(id)
        if blog :
            blog.delete_from_db()
        return {'message' : 'blog deleted'}

    def put(self, id):
        data = BlogModel.parser.parse_args()
        blog = BlogModel.find_blog_by_id(id)
        if blog :
            blog.title = data["title"]
            blog.title = data["content"]
            blog.user_id = data["user_id"]
        else :
            blog = BlogModel(id, **data)
        blog.save_to_db()

        return blog.json()


class BlogList(Resource):
    def get(self):
        return { 'blogs' : [blog.json() for blog in BlogModel.get_blogs() ] }