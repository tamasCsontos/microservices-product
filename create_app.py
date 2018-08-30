import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Application:
    app = None
    db = None

    def __init__(self):
        if not self.app and not self.db:
            self.app = Flask('Magic')
            self.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
            self.db = SQLAlchemy(self.app)


application = Application()
