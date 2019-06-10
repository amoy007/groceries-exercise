# groceries-exercise
second coding project!


## Repo Setup
1. On github.com, created a new repository called groceries-exercise. Set it up with readme file, Python-based .gitignore file, and MIT license. 
2. Click "clone or download" green button, and then click "Open on Desktop. Once Github Desktop opens up, click Repository tab > Open in Git Bash.
3. In Git Bash, type on command line to create a "groceries" file. 
'''touch groceries.py
4. Open the repo in Visual Code Editor. In the new groceries.py file, Add the following text into per https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/exercises/groceries/README.md
'''# groceries.py
'''
'''#from pprint import pprint
'''
'''products = [
'''    {"id":1, "name": "Chocolate Sandwich Cookies", "department": '''"snacks", "aisle": "cookies cakes", "price": 3.50},
'''    {"id":2, "name": "All-Seasons Salt", "department": "pantry", '''"aisle": "spices seasonings", "price": 4.99},
'''    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", '''"department": "beverages", "aisle": "tea", "price": 2.49},
'''    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni '''With Vodka Cream Sauce", "department": "frozen", "aisle": '''"frozen meals", "price": 6.99},
'''    {"id":5, "name": "Green Chile Anytime Sauce", "department": '''"pantry", "aisle": "marinades meat preparation", "price": 7.99}''',
'''    {"id":6, "name": "Dry Nose Oil", "department": "personal care",''' "aisle": "cold flu allergy", "price": 21.99},
'''    {"id":7, "name": "Pure Coconut Water With Orange", '''"department": "beverages", "aisle": "juice nectars", "price": '''3.50},
'''    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", '''"department": "frozen", "aisle": "frozen produce", "price": '''4.25},
'''    {"id":9, "name": "Light Strawberry Blueberry Yogurt", '''"department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
'''    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear '''Beverage", "department": "beverages", "aisle": "water seltzer '''sparkling water", "price": 2.99},
'''    {"id":11, "name": "Peach Mango Juice", "department": '''"beverages", "aisle": "refrigerated", "price": 1.99},
'''    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": '''"frozen", "aisle": "frozen dessert", "price": 18.50},
'''    {"id":13, "name": "Saline Nasal Mist", "department": "personal '''care", "aisle": "cold flu allergy", "price": 16.00},
'''    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", '''"department": "household", "aisle": "dish detergents", '''"price": 4.99},
'''    {"id":15, "name": "Overnight Diapers Size 6", "department": '''"babies", "aisle": "diapers wipes", "price": 25.50},
'''    {"id":16, "name": "Mint Chocolate Flavored Syrup", '''"department": "snacks", "aisle": "ice cream toppings", '''"price": 4.50},
'''    {"id":17, "name": "Rendered Duck Fat", "department": "meat '''seafood", "aisle": "poultry counter", "price": 9.99},
'''    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", '''"department": "frozen", "aisle": "frozen pizza", "price": '''12.50},
'''    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom '''Blend", "department": "dry goods pasta", "aisle": "grains rice '''dried goods", "price": 3.99},
'''    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich '''Drink", "department": "beverages", "aisle": "juice nectars", '''"price": 4.25}
'''] # based on data from Instacart: https://www.instacart.com/'''datasets/grocery-shopping-2017
'''
'''print(products)
'''# pprint(products)
'''
'''# TODO: write some Python code here to produce the desired output

## Environment Setup
1. Create and activate a new Anaconda virtual environment:

'''conda create -n groceries-env python=3.7 # (first time only)
'''conda activate groceries-env

2. From within the virtual environment, install the pytest package:

# NOTE: we won't need pytest until/unless addressing the optional "Automated Testing" challenge,
# so you can feel free to skip this now and return later...

'''pip install pytest

3. From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

'''python groceries.py
