from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# PUT ABSOLUTE PATH TO UPLOAD FOLDER ON SERVER HERE
app.config['UPLOAD_FOLDER'] = "/UPLOAD_FOLDER/"

from hackThisPage import views

app.config.from_object('config')
