__author__ = 'SolPie'

from flask import Blueprint, render_template
from models import Uppo

route_uppo = Blueprint('uppo', __name__, template_folder='../templates/pixtch/uppo')


def get_uppo(pid):
    return Uppo.query.filter(Uppo.id == pid).first()


@route_uppo('/p/<int:pid>')
def uppo_view(pid):
    if pid:
        uppo = get_uppo(pid)
        return render_template('detail.html', uppo=uppo)
    else:
        render_template('list.html')
