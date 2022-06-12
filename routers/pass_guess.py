import base64

import flask


def send_video() -> flask.Response:
    with open('./static/video/cumshot.webm', 'rb') as stream:
        b64 = base64.b64encode(stream.read())
        return flask.Response(b64, content_type='video/webm', status=201)


pass_router = flask.Blueprint('pass', __name__, url_prefix='/password')


@pass_router.get('/')
def main():
    return flask.render_template('pass.html')


@pass_router.get('/check')
def check_pass():
    real_pass = 'OralCumshot'
    correct = ''
    password = flask.request.args.get('pass')
    for i, vals in enumerate(zip(password, real_pass)):
        if vals[0] == vals[1]:
            correct += vals[0]
        else:
            correct += '_'
    if len(correct) < len(real_pass):
        correct += '_' * (len(real_pass) - len(correct))
    if '_' in correct:
        return correct[:len(real_pass)], 200
    return send_video()
