import flask
import logging

test_router = flask.Blueprint('test', __name__, url_prefix='/test')


@test_router.post('/')
def main():
    logging.info(flask.request.data)
    logging.info(flask.request.data.decode('utf-8'))
    try:
        with open('./log.txt', 'a', encoding='utf-8') as file:
            file.write(flask.request.data.decode('utf-8'))
    except:
        pass
    return flask.request.json, 200
