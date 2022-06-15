import flask


chat_router = flask.Blueprint('chat', __name__, url_prefix='/chat')


@chat_router.get('/')
def main():
    return flask.render_template('chat.html')
