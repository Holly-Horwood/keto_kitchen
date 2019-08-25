import os

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY')
    #MONGO_URI = os.environ.get('MONGO_URI')
    MONGO_URI = "mongodb+srv://nz_user:Reef5115@myfirstcluster-clbrq.mongodb.net/keto_kitchen?retryWrites=true&w=majority"
    