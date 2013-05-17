__author__ = 'SolPie'
# -*- coding:utf-8 -*-
#################################################
import os

if 'SERVER_SOFTWARE' in os.environ:
    uri = os.environ.get('MYSQL')
    print "This is online environ"
else:
    uri = 'sqlite:///db/test.db'
    print "This is local environ"
##################################################

#####################new##################
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


######################
def autogenerate():
    'alembic revision --autogenerate -m "Added account table"'
    pass


def upgrade():
    'alembic upgrade head'
    pass


if __name__ == '__main__':
    pass
