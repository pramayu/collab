from flask import Blueprint

homepage = Blueprint('homepage', __name__, None)

@homepage.route('/')
def index():
	return '😜'