__author__ = 'SolPie'

import time
import sys

sys.path.insert(0, 'libs')
import os
import json
from flask import Flask, Request, Response, url_for, render_template, request, session, flash, redirect, g, abort

application = app = Flask(__name__)
#
# @app.route('/')
# def welcome():
#     return render_template('pixtch/index.html')
@app.before_request
def before_request():
    # g.db = connect_db()
    pass

from database import db_session


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
    pass


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('static/upload/upload.txt')


@app.route('/uppo/<upponame>')
def show_uppo_profile(upponame):
    return 'uppo %s' % upponame


@app.route('/env')
def env():
    return os.environ.get("VCAP_SERVICES", "{}")


@app.route('/show')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('pixtch/postDetail.html', entries=entries)








'''
error
'''


@app.errorhandler(404)
def error404(error):
    return render_template('404.html')


'''
init
'''


def init_bluePrint():
    from auth.views import route_auth

    # app.register_blueprint(route_auth)
    app.register_blueprint(route_auth, url_prefix='/login')
    from kn.views import route_kn

    app.register_blueprint(route_kn, url_prefix='/kn')
    from admin.views import mod as admin

    # app.register_blueprint(admin)
    app.register_blueprint(admin, url_prefix='/admin')


    pass


def init_database():
    from database import init_db

    init_db()


def init_admin():
    from flask.ext.admin import Admin
    from flask.ext.admin.contrib.sqlamodel import ModelView

    admin = Admin(app, name='Pixtch Backend')
    from kn.models import User
    from database import db_session

    admin.add_view(ModelView(User, db_session))


if __name__ == '__main__':
    init_database()
    init_bluePrint()
    init_admin()
    # from test import bp
    # app.register_blueprint(bp)
    print 'init_end'
    # print app.url_rule_class.alias
    #
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)

