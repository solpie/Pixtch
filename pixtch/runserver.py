# -*- coding:utf-8 -*-
__author__ = 'SolPie'
import os
from flaskPixtch import create_app


if __name__ == '__main__':
    #todo http://markitup.jaysalvat.com/home/
    #todo flask-sqlalchemy
    # http://developer.baidu.com/wiki/index.php?title=docs/cplat/rt/python/faq
    app = create_app()

    from database import db

    db.init_app(app)
    # db.create_all()

    import datetime

    t = datetime.datetime.now()
    app.setup()
    print __name__, '>>init..ok', t, app.secret_key
    # print app.url_rule_class.alias
    #
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)

