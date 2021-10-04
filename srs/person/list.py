from flask import Blueprint
from flask import render_template
from .person import Person

person_list = Blueprint('person_list', __name__)


@person_list.route('/')
@person_list.route("/person")
def index():
    persons = [Person("qwe", "qwe", "ert")]
    return render_template("person/list.html", persons=persons)
