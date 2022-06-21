import flask

test_router = flask.Blueprint('test', __name__, url_prefix='/test')


@test_router.get('/')
def main():
    try:
        print(flask.data)
        with open('./log.txt', 'a', encoding='utf-8') as file:
            file.write(flask.data)
    except:
        pass
    return flask.json, 200
