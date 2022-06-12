import flask
import flask_cors

from routers import *

app = flask.Flask(__name__)
flask_cors.CORS(app)
app.register_blueprint(pass_router)
app.register_blueprint(phrase_router)


@app.route('/')
def main():
    return flask.render_template('main.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5555, debug=True)
