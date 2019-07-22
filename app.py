#!/usr/bin/python
import os
import boto3
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
def home():
    return render_template('index.html', recipes=mongo.db.recipes.find())

#Gets id for requested recipe and renders the full recipe template
@app.route('/full_recipe/<recipe_id>')   
def full_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('fullrecipe.html', recipe=the_recipe)

#Gets blank form to add recipe, once completed posts to add then redirects to home page.
@app.route('/add_recipe', methods=['GET', 'POST']) 
def insert_recipe():
    if request.method == 'GET':
        return render_template('addrecipe.html')
    else:    #user has submitted the form:
        s3_resource = boto3.resource('s3') #connection to S#
        keto_bucket = s3_resource.Bucket("ketokitchen") #connection to keto bucket in S3
        image_file = request.files['image_file'] 
        keto_bucket.Object(image_file.filename).put(Body=image_file)  #putting the file into our S3 bucket
        TODO:USE CURRENT DATE AND TIME TO MILLISECONDS TO MAKE A UNIQUE FILE NAME
        url = "https://ketokitchen.s3-ap-southeast-2.amazonaws.com/" + image_file.filename    #create a URL for the uploaded image in the bucket
        recipes = mongo.db.recipes
        recipe_dict = request.form.to_dict()
        recipe_dict.update( {'image_url' : url} ) #appends image_url to the other form data
        recipes.insert_one(recipe_dict) #adds recipe to database as key value pairs
    return redirect(url_for('home'))

#Gets form to edit recipe, once completed posts to update then redirects to home page.
@app.route('/edit_recipe', methods=['GET', 'POST']) 
def edit_recipe():
    if request.method == 'GET':
        return render_template('editrecipe.html')
    else:
        recipes = mongo.db.recipes
        recipes.insert_one(request.form.to_dict())
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)