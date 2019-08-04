#!/usr/bin/python
import os, datetime
import boto3
import pymongo
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from config import Config
from pymongo import MongoClient
from bson.objectid import ObjectId


# Init App
app = Flask(__name__)
app.config.from_object(Config)

# MongoDB URI 
client = MongoClient(Config.MONGO_URI)
db = client.keto_kitchen

mongo = PyMongo(app)

# Home Page

@app.route('/')
def home():
    return render_template('index.html', recipes=mongo.db.recipes.find().sort('date', pymongo.DESCENDING))

#Gets id for requested recipe and renders the full recipe template when full recipe link is clicked on in index.html
@app.route('/full_recipe/<recipe_id>')   
def full_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    #searches fields and splits array at the pipes
    ingredients_split = the_recipe['ingredients'].split('|')
    method_split = the_recipe['method'].split('|')
    return render_template('fullrecipe.html', recipe=the_recipe, ingredients=ingredients_split, method=method_split)

#Gets blank form to add recipe, once completed posts to add then redirects to home page.
@app.route('/add_recipe', methods=['GET', 'POST']) 
def insert_recipe():
    if request.method == 'GET':
        return render_template('addrecipe.html')
    else:    #user has submitted the form:
        s3_resource = boto3.resource('s3') #connection to S3
        keto_bucket = s3_resource.Bucket("ketokitchen") #connection to keto bucket in S3
        now = datetime.datetime.now() #creates time-stamp string for file names
        now_string = str(now.strftime("%d-%m-%Y_%H%M%S"))
        image_file = request.files['image_file'] 
        full_file_name = (now_string + image_file.filename)
        keto_bucket.Object(full_file_name).put(ACL='public-read', Body=image_file, ContentType='image/jpeg')  #putting the file into our S3 bucket
        url = "https://ketokitchen.s3-ap-southeast-2.amazonaws.com/" + full_file_name   #create a URL for the uploaded image in the bucket
        recipes = mongo.db.recipes
        recipe_dict = request.form.to_dict()
        recipe_dict.update( {'image_url' : url} ) #appends image_url to the other form data
        recipe_dict.update( {'date' : now}) # appends date recipe is created
        recipe_dict['ingredients'] = request.form['ingredients'].replace('\n', '|') #takes whats added by user and replaces | with new lines
        recipe_dict['method'] = request.form['method'].replace('\n', '|')
        recipe_dict['diet'] = request.form.getlist('diet') #saves all values from diet checkboxes
        recipes.insert_one(recipe_dict) #adds recipe to database as key value pairs
    return redirect(url_for('home'))

@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST']) 
def edit_recipe(recipe_id):
    if request.method == 'GET':
        the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        print(the_recipe)
        #searches fields and splits array at the pipes
        ingredients_edit = the_recipe['ingredients'].replace('|', '\n')
        method_edit = the_recipe['method'].replace('|', '\n')
        return render_template('editrecipe.html' , recipe=the_recipe, ingredients=ingredients_edit, method=method_edit)  
    return redirect(url_for('home'))

   


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)