from flask import Flask, request, render_template, send_from_directory
import os
import json

from uuid import uuid4

from database import db_session
from models import File
from upload import app, UPLOAD_FOLDER, files_upload

@app.route("/")
def index():
    files = db_session.query(File).all()
    return render_template("index.html", files=files)

@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory=app.config['UPLOADED_FILES_DEST'], filename=filename)

@app.route("/uikit")
def uikit():
    files = db_session.query(File).all()
    return render_template("uikit.html", files=files)    

@app.route("/uikitprogress")
def uikitprogress():
    return render_template("uikitprogress.html")     

@app.route("/upload", methods=["POST"])
def upload():

    form = request.form    
    target = UPLOAD_FOLDER

    for upload in request.files.getlist("file"):
        
        unique = str(uuid4())        
        filename, ext = os.path.splitext(upload.filename)    

        newname = unique + ext

        destination = "/".join([target, newname])

        f = File()
        f.name_readlabe = upload.filename
        f.name = newname
        db_session.add(f)
        db_session.commit()

        upload.save(destination)
    
    return ajax_response(True, destination)

def ajax_response(status, msg):
    status_code = "ok" if status else "error"
    return json.dumps(dict(
        status=status_code,
        msg=msg,
    ))



