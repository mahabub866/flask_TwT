from flask import Flask,request
from flask_restful import Api, Resource,reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

video_put_args=reqparse.RequestParser()
video_put_args.add_argument('name', type=str,help="Name of the video")
video_put_args.add_argument('likes', type=int,help="likes of the video")
video_put_args.add_argument('views', type=int,help="views on the video")

videos={}
class HelloWord(Resource):
    def get(self):
        return {"data": "world"}
class HelloWordParam(Resource):
    def get(self,name):
        return {"data": name}
class Viceo(Resource):
    def get(self,video_id):
        return videos[video_id]
    def put(self,video_id):
        # print(request.form)
        args=video_put_args.parse_args()
        videos[video_id]=args
        return videos[video_id],201
        
api.add_resource(HelloWord,"/")
api.add_resource(HelloWordParam,"/<string:name>")
api.add_resource(Viceo,"/video/<string:video_id>")
if __name__ == "__main__":
	app.run(debug=True)