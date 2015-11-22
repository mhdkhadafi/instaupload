import sqlite3
from flask import Flask, request, redirect, render_template, g, jsonify, flash, url_for
from contextlib import closing
import datetime
from application import db
from application.models import Colors
from instagram import uploadPhoto

# configuration
import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# DATABASE = '/tmp/color.db'
DEBUG = True

app = Flask(__name__)
app.secret_key = "instaupload"
app.config.from_object(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            uploadPhoto(os.path.join(app.config['UPLOAD_FOLDER']) + filename)
            return redirect('/')
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/show')
def show_picture():
	return '''
	<!doctype html>
	<img src="./tmp/h3.png">
	'''


if __name__ == '__main__':
	app.run()

