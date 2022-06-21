import flask

test_router = flask.Blueprint('test', __name__, url_prefix='/test')


@test_router.post('/')
def main():
    try:
        print(flask.request.data.decode('utf-8'))
        with open('./log.txt', 'a', encoding='utf-8') as file:
            file.write(flask.request.data.decode('utf-8'))
    except:
        pass
    return flask.request.json, 200
