from flask import render_template
from flask_login import login_required

from . import admin


@admin.route('/', methods=['GET'])
@login_required
def index():
    return render_template("admin/index.html")
