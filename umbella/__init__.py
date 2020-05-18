# import flask from the package imported moduls calss
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

#instantiate the database with SQLAlchemy
db = SQLAlchemy()

# this is the name of module/package that is calling this app
app = Flask(__name__)

# create a function that create a web application
# a web server will run this application
def create_app():
    app.debug = True
    app.secret_key = 'UmbellaSecretKeyN10669710'

    #set the app configuration data
    app.config['SQLAlLCHEMY_DATABASE_URL'] = 'sqlite:///umbella.sqlite'

    # initialize db with flask
    db.init_app(app)
    
    bootstrap = Bootstrap(app)
    
    # importing modules here to avoid circular references, register blueprints of routes
    # add the Blueprint
    from . import views
    app.register_blueprint(views.bp)

    return app


@app.errorhandler(404)
# inbult function witch taks error as parameter
def not_found(e):
    return render_template("404.html")


@app.errorhandler(505)
# inbult function witch taks error as parameter
# handle server issue
def internal_error(e):
    return render_template("505.html")




