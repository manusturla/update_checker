from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from flask_cors import CORS
from flask_migrate import Migrate

#######################
#### Configuration ####
#######################

# Create the instances of the Flask extensions (flasky, flask-login, etc.) in
# the global scope, but without any arguments passed in.  These instances are not attached
# to the application at this point.
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
# scheduler_helper = SchedulerHelper()

######################################
#### Application Factory Function ####
######################################


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile(config_filename)
    db.init_app(app)
    migrate.init_app(app, db)
    from project.routes import base_blueprint

    app.register_blueprint(base_blueprint)
    app.logger.info(f"SQLALCHEMY_DATABASE_URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    return app
