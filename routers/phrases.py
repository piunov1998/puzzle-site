import base64

import flask

phrase_router = flask.Blueprint('phrases', __name__, url_prefix='/phrases')
phrase = [
    'le', 'te a', 'ele', "t's c", 'bra', ' som', 'ick', 'nd s', 'e d', 'uck']


def send_video() -> flask.Response:
    with open('./static/video/celebrate.webm', 'rb') as stream:
        b64 = base64.b64encode(stream.read())
        return flask.Response(b64, content_type='video/webm', status=201)


@phrase_router.get('/')
def main():
    return flask.render_template('phrases.html')


@phrase_router.get('/check')
def check():
    ints = flask.request.args.get('pass')
    if not ints.isnumeric():
        return 'Ну ты долбаеб?', 400
    resp = ''.join([phrase[int(i)] for i in ints])
    if resp == "let's celebrate and suck some dick":
        return send_video()
    else:
        return resp, 200
