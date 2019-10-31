import os
from flask import Flask, Blueprint

app = Flask(__name__, instance_relative_config=True)

current_folder = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(current_folder, "upload")

from scrapeThisPage import views

from routes import api_v1
app.register_blueprint(api_v1.blueprint, url_prefix="/api/")
