import unittest 
from app import search_recipes, app
from flask import Flask


class SearchTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass    

    def test_that_recipe_search_returns_breakfast(self):
        cuisineSelected = ""
        courseSelected = ["Breakfast"]
        dietSelected = []
        recipe_results = search_recipes(cuisineSelected, courseSelected, dietSelected)
        results = list(recipe_results)
        assert len(results) != 0 and "Breakfast" in results[0]["course"], "Should be at least one Breakfast recipe"

    def test_that_recipe_search_returns_british(self):
        cuisineSelected = "British"
        courseSelected = []
        dietSelected = []
        recipe_results = search_recipes(cuisineSelected, courseSelected, dietSelected)
        results = list(recipe_results)
        assert len(results) != 0 and "British" in results[0]["cuisine"], "Should be at least one British recipe"  

    def test_that_recipe_search_returns_keto(self):
        cuisineSelected = ""
        courseSelected = []
        dietSelected = ["Keto"]
        recipe_results = search_recipes(cuisineSelected, courseSelected, dietSelected)
        results = list(recipe_results)
        assert len(results) != 0 and "Keto" in results[0]["diet"], "Should be at least one Keto recipe"      

class WebTests(unittest.TestCase):
    
    def setUp(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.client = app.test_client()

    def tearDown(self):
        pass 

# Test that the add_recipe page can be found
    def test_that_add_recipe_page_found(self):
        response = app.test_client(self).get('/add_recipe', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "add_recipe returned status code %s should be 200" % str(response.status_code)) 
 # Coph abpve and try for different pages, id will be needed for edit and full recipe ie '/edit_recipe/52156632566'  TODO: to run test python test.py


if __name__=="__main__":
    unittest.main()
