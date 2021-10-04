from flask import Blueprint
from flask import render_template

from .person import Person

person_detail = Blueprint('person_detail', __name__)


@person_detail.route('/person/<id>')
def index(id):
    person = Person("qwe", "qwe", "ert")
    return render_template("person/detail.html", person=person)

    # return redirect(url_for("index"))
