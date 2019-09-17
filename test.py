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

    def test_that_add_recipe_page_found(self):
        response = app.test_client(self).get('/add_recipe', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "add_recipe returned status code %s should be 200" % str(response.status_code)) 


    def test_that_edit_recipe_page_found(self):
        response = app.test_client(self).get('/edit_recipe/5d58f86d4f2214bd76ef9a21', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "edit_recipe returned status code %s should be 200" % str(response.status_code))


    def test_that_full_recipe_page_found(self):
        response = app.test_client(self).get('/full_recipe/5d58f86d4f2214bd76ef9a21', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "full_recipe returned status code %s should be 200" % str(response.status_code))


    def test_that_results_page_found(self):
        response = app.test_client(self).get('/display_results?course=Main&course=&cuisine=&diet=Low+Carb&diet=', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "display_results returned status code %s should be 200" % str(response.status_code)) 


    def test_that_index_page_found(self):
        response = app.test_client(self).get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "index page returned status code %s should be 200" % str(response.status_code))       

if __name__=="__main__":
    unittest.main()
