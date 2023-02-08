import os

import flask
import flask_cors

from routers import *

app = flask.Flask(__name__)
flask_cors.CORS(app)
app.register_blueprint(pass_router)
app.register_blueprint(phrase_router)
app.register_blueprint(chat_router)
app.register_blueprint(test_router)


@app.route('/')
def main():
    return flask.render_template('main.html')


if __name__ == '__main__':
    host = os.getenv('APP_HOST', '0.0.0.0')
    port = os.getenv('APP_PORT', 80)
    app.run(host, port=port)
