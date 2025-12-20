from flask import Blueprint
from app.routes.handlers import (
    index_handler,
    resume_upload_handler,
    upload_resume_handler,
    analyse_handler,
    recommender_handler,
)

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return index_handler()


@bp.route('/resume_upload')
def resume_upload():
    return resume_upload_handler()


@bp.route('/upload_resume', methods=['POST'])
def upload_resume():
    return upload_resume_handler()


@bp.route('/analyse')
def analyse():
    return analyse_handler()


@bp.route('/recommender')
def recommender():
    return recommender_handler()
