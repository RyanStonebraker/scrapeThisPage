import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)

current_folder = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(current_folder, "upload")
app.config.from_object('config')

from hackThisPage import views
