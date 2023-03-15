# from flask import Flask,request
# from flask_restful import Api, Resource,reqparse
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# api = Api(app)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # db = SQLAlchemy(app)

# video_put_args=reqparse.RequestParser()
# video_put_args.add_argument('name', type=str,help="Name of the video")
# video_put_args.add_argument('likes', type=int,help="likes of the video")
# video_put_args.add_argument('views', type=int,help="views on the video")

# videos={}
# class HelloWord(Resource):
#     def get(self):
#         return {"data": "world"}
# class HelloWordParam(Resource):
#     def get(self,name):
#         return {"data": name}
# class Viceo(Resource):
#     def get(self,video_id):
#         return videos[video_id]
#     def put(self,video_id):
#         # print(request.form)
#         args=video_put_args.parse_args()
#         videos[video_id]=args
#         return videos[video_id],201
        
# api.add_resource(HelloWord,"/")
# api.add_resource(HelloWordParam,"/<string:name>")
# api.add_resource(Viceo,"/video/<string:video_id>")
# if __name__ == "__main__":
# 	app.run(debug=True)














from flask import Flask, json, request, jsonify
import os
import urllib.request
from werkzeug.utils import secure_filename
 
app = Flask(__name__)
 
app.secret_key = "caircocoders-ednalan"
 
UPLOAD_FOLDER = 'files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
@app.route('/')
def main():
    return 'Homepage'
 
@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'files[]' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
 
    files = request.files.getlist('files[]')
     
    errors = {}
    success = False
     
    for file in files:      
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success = True
        else:
            errors[file.filename] = 'File type is not allowed'
 
    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        resp = jsonify({'message' : 'Files successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
 
if __name__ == '__main__':
    app.run(debug=True)