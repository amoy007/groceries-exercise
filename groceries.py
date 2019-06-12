# groceries.py

from pprint import pprint

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


#curly braces tell you it's a dictionary. each one is a dictionary. Read about dictionaries here: https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/datatypes/dictionaries.md
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

products_count = len(products) #read about lists here: https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/datatypes/lists.md

print("--------------")

# you can use print(f"one string {products_count} another string:")
# print(f"THERE ARE {products_count} PRODUCTS:")
print("THERE ARE",{products_count},"PRODUCTS:")

# or you can do print("one string" + products_count + "another string:")
# or you can do print("one string",products_count,"another string:")


print("--------------")



def sort_by_name(any_product):
    return any_product['name']

sorted_products = sorted(products, key=sort_by_name)



for item in sorted_products: #you named each list in the dictionary as "item" so you can print(type[item]) --- it is a dictionary data type.
    #print(item["name"]) 
    #print(item["name"]) <<<use rectangle brackets to reference items in a dictionary.
    #n = item["name"]
    #price = item["price"]
    #print(f"{item['name']} ... ${item['price']}") <<Concatenate using the f formula.
    
    price_usd = to_usd(item['price'])
    print(f"+ {item['name']} ({price_usd})")

print("--------------")

# Creating a filter
# arr = [1, 2, 3, 4]
# arr2 = []
# for i in arr:
#   arr2.append(i * 100)

departments = []

for newline in products:
    #print(newline["department"])
    departments.append(newline["department"])
    
    #if newline["department"] not in departments:
    #    departments.append(newline["department"])

unique_departments = list(set(departments))

#department_count = len(somelist)
department_count = len(unique_departments)

print(f"THERE ARE {department_count} DEPARTMENTS:")
print("--------------")

unique_departments.sort()

product_subtotal = "1"

for d in unique_departments:
    print(f"{d.title()} ({product_subtotal} product)") #makes the result into Title Case. Refer to https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/datatypes/strings.md
    



#print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output




# breakpoint()
# breakpoint() allows you to start testing/working within the program using a command line software like Git Bash.
# you can test pdb using the following command line filters
# [p for p in products if p["department"] == "snacks"]
# [p for p in products if p["id"] == 4]
# and for one that returns an error:
# 