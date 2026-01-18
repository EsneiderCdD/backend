from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def status():
        return "Backend4 Running with Flask CLI"
    return app
