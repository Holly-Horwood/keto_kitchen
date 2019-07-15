import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from config import Config
from pymongo import MongoClient
from bson.objectid import ObjectId

# Init App
app = Flask(__name__)
app.config.from_object(Config)

# MongoDB URI / Assign db
client = MongoClient(Config.MONGO_URI)
db = client.keto_kitchen

mongo = PyMongo(app)

# Home Page

@app.route('/')
def recipes():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())

@app.route('/full_recipe/<recipe_id>')   
def full_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('fullrecipe.html', recipe=the_recipe)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)