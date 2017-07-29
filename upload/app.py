from flask import Flask, request, render_template
import os
import json
from uuid import uuid4

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/uikit")
def uikit():
    return render_template("uikit.html")    

@app.route("/uikitprogress")
def uikitprogress():
    return render_template("uikitprogress.html")     

@app.route("/upload", methods=["POST"])
def upload():

    form = request.form    
    target = "upload/static/uploads/"    

    for upload in request.files.getlist("file"):
        
        unique = str(uuid4())        
        filename, ext = os.path.splitext(upload.filename)        
        destination = "/".join([target, (unique + ext)])
        upload.save(destination)
    
    return ajax_response(True, destination)

def ajax_response(status, msg):
    status_code = "ok" if status else "error"
    return json.dumps(dict(
        status=status_code,
        msg=msg,
    ))
