import logging

import flask

test_router = flask.Blueprint('test', __name__, url_prefix='/test')
logging.basicConfig(level=logging.INFO)


@test_router.post('/')
def main():
    logging.info(flask.request.headers)
    logging.info(flask.request.data)
    logging.info(flask.request.data.decode('utf-8'))
    return flask.request.json, 200
