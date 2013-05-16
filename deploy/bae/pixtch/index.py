# -*- coding: utf-8 -*-
__author__ = 'SolPie'
from bae.core.wsgi import WSGIApplication

import sys
import os


from bae.core.const import *

user, pw, host, port, db = MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, 'MVwslEoiYLtUAerKTSuE'
uri = "mysql://%s:%s@%s:%s/%s" % (
    user,
    pw,
    host,
    port,
    db)
os.environ.setdefault('MYSQL', uri)
print "This is BAE environ"

sys.path.insert(0, os.path.join('.', 'site-packages'))
from runserver import app
app.setup()
# app.init_db(MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, 'MVwslEoiYLtUAerKTSuE')
application = WSGIApplication(app)
