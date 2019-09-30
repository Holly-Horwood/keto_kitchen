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
    return render_template('index.html', recipes=mongo.db.recipes.find().sort('date', pymongo.DESCENDING), courses=mongo.db.courses.find(), cuisines=mongo.db.cuisines.find(), diets=mongo.db.diets.find())

#Gets id for requested recipe and renders the full recipe template when full recipe link is clicked on in index.html
@app.route('/full_recipe/<recipe_id>')   
def full_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    #searches fields and splits array at the pipes
    ingredients_split = the_recipe['ingredients'].split('|')
    method_split = the_recipe['method'].split('|')
    dietString = ", ".join(the_recipe['diet'])
    courseString = ", ".join(the_recipe['course'])
    return render_template('fullrecipe.html', recipe=the_recipe, ingredients=ingredients_split, method=method_split, dietString=dietString, courseString=courseString)

# Add and Edit Pages
def update(is_edit, recipe_id=0 ):
    recipe_dict = request.form.to_dict()
    now = datetime.datetime.now() #creates time-stamp string for file names
    recipe_dict.update( {'date' : now}) # appends date recipe is created
    
    if 'image_file' in request.files and request.files['image_file'].filename:#This line courtesy of Dick Vlaanderen
        image_file = request.files['image_file'] 
        s3_resource = boto3.resource('s3') #connection to S3
        keto_bucket = s3_resource.Bucket("ketokitchen") #connection to keto bucket in S3       
        now_string = str(now.strftime("%d-%m-%Y_%H%M%S"))
        full_file_name = (now_string + image_file.filename)
        keto_bucket.Object(full_file_name).put(ACL='public-read', Body=image_file, ContentType='image/jpeg')  #putting the file into our S3 bucket
        url = "https://ketokitchen.s3-ap-southeast-2.amazonaws.com/" + full_file_name   #create a URL for the uploaded image in the bucket
        recipe_dict.update( {'image_url' : url} ) #appends image_url to the other form data
    
    else:
        if is_edit:
            the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
            recipe_dict.update( {'image_url' : the_recipe['image_url']} )


    recipes = mongo.db.recipes
    recipe_dict['ingredients'] = request.form['ingredients'].strip().replace('\r\n', '|') #takes whats added by user and replaces | with new lines
    recipe_dict['method'] = request.form['method'].strip().replace('\r\n', '|')
    recipe_dict['diet'] = request.form.getlist('diet')
    recipe_dict['course'] = request.form.getlist('course') #saves all values from checkboxes
    if is_edit:
        recipes.update_one({'_id':ObjectId(recipe_id)}, {"$set": recipe_dict}, upsert=False) #updates recipe in database
    else:
        recipes.insert_one(recipe_dict) #adds recipe to database as key value pairs

#Gets blank form to add recipe, once completed posts to add then redirects to home page.
@app.route('/add_recipe', methods=['GET', 'POST']) 
def add_recipe():
    if request.method == 'GET':
        return render_template('addrecipe.html', courses=mongo.db.courses.find(), cuisines=mongo.db.cuisines.find(), diets=mongo.db.diets.find())
    else:    #user has submitted the form:
        update(False)
    return redirect(url_for('home'))

#Gets full recipe in an editable form for updating then redirects to home page once posted
@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST']) 
def edit_recipe(recipe_id):
    if request.method == 'GET':
        the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        #searches fields and splits array at the pipes
        ingredients_edit = the_recipe['ingredients'].replace('|', '\n')
        method_edit = the_recipe['method'].replace('|', '\n')
        return render_template('editrecipe.html', recipe=the_recipe, ingredients=ingredients_edit, method=method_edit, courses=mongo.db.courses.find(), cuisines=mongo.db.cuisines.find(), diets=mongo.db.diets.find()) 
    else:
        update(True, recipe_id)
        return redirect(url_for('home'))

#Searches for recipes with matching data
def search_recipes(cuisineSelected, courseSelected, dietSelected):
    query = {}
    if (cuisineSelected): # appends to query the users selected cuisine
        query.update({'cuisine' : cuisineSelected})

    # if user has made a selection appends to query
    if len(list(courseSelected)) != 0 and courseSelected[0] != "":
        query.update({'course' : {"$in": courseSelected} })

    if len(list(dietSelected)) != 0 and dietSelected[0] != "":
        query.update({'diet' : {"$in": dietSelected} })

    return mongo.db.recipes.find(query)

#Display search results page based on user selections
@app.route("/display_results", methods=['GET'])
def display_results():
    #read in user selections from query string
    courseSelected = request.args.getlist('course')
    cuisineSelected = request.args['cuisine']
    dietSelected = request.args.getlist('diet')

    recipe_results = search_recipes(cuisineSelected, courseSelected, dietSelected)

    return render_template("results.html", recipes=recipe_results, courses=mongo.db.courses.find(), cuisines=mongo.db.cuisines.find(), diets=mongo.db.diets.find(), courseSelected=courseSelected, cuisineSelected=cuisineSelected, dietSelected=dietSelected) #executes the query

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('home'))   
  

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=int(os.environ.get('PORT', '8080')),
            debug=False)