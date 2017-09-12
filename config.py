import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_dir = basedir + '\Database'


# IP adress is not really important, it takes the port with rsplit if port is not
# mentioned in app.run parameters.
SERVER_NAME = "127.0.0.1:5001"
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(db_dir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(db_dir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = False
#SECRET_KEY = 'irdeto'

#This variable is used in setting the theme directory in html and css files
#Possible values are: basic, fancy
THEME = 'fancy'
#THEME = 'basic'
