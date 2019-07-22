import os

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGO_URI = os.environ.get('MONGO_URI')

    S3_KEY = os.environ.get('S3_KEY')
    S3_SECRET = os.environ.get('S3_SECRET')