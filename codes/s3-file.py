from flask import Flask,render_template,request
import boto3
from werkzeug.utils import secure_filename
app=Flask(__name__)
s3_resource = boto3.resource('s3')
BUCKET_NAME = "flask-s3-33"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3_resource.Object(BUCKET_NAME, filename).upload_file(Filename=filename)
msg = "Upload Done ! "

return render_template("index.html",msg =msg)




if __name__ == "_main_":
    app.run(debug=True,port=8080)