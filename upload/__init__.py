from flask import Flask
import os

app = Flask(__name__)

from flask_uploads import configure_uploads
from flask_uploads import UploadSet

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
app.config['UPLOADED_FILES_DEST'] = UPLOAD_FOLDER

files_upload = UploadSet('files', )

configure_uploads(app, (files_upload,))

