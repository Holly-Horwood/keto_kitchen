import unittest
from app import search_recipes

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
        pass

    def tearDown(self):
        pass 



if __name__=="__main__":
    unittest.main()
