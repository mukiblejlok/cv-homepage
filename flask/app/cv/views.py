import json
import os

from flask import render_template
from flask_login import login_required

from . import cv

CV_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'static', 'cv_json'))


@cv.route("/", methods=["GET"])
@cv.route("/user/<user_uuid>", methods=["GET"])
def user_cv(user_uuid: str = '1'):
    cv_path = os.path.join(CV_DATA_PATH, f'user_{user_uuid}.json')
    with open(cv_path, 'r') as file:
        data = json.load(file)
    return render_template("cv/user_cv.html", data=data)
