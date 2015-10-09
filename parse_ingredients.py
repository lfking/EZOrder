import re

__author__ = 'eitanz'
food_type_data = [
    (['tomato', 'tomatoes', 'fresh tomatoes'], False, True, 'g', {
            'cup': 200,
            'single' : 150
        }, [
            ('tomatoes by weight', 99, 500, 'g')
        ]
    ),
    (['crushed tomato', 'tomato sauce', 'tomatoes sauce', 'fresh tomatoes sauce'], False, False, 'g', {
        'cup': 300,
        'single':200
        }, [
            ('100g osem tomato sauce', 120, 100, 'g'),
            ('200g osem tomato sauce    ', 200, 200, 'g')
        ]
    ),
    (['egg', 'eggs'], False, False, 'carton', {}, [
            ('6 pack free range eggs', 1500, 6, ''),
            ('12 pack free range eggs', 2000, 12, ''),
            ('6 pack eggs', 1000, 6, ''),
            ('12 pack eggs', 1600, 12, '')
        ]
    ),
    (['flour'], False, False, 'g', {
            'cup': 400,
        }, [
            ('regular flour', 1000, 1000, 'g')
        ]
    ),
    (['onion', 'onions'], False, True, 'g', {
            'cup': 200,
            'single' : 150
        }, [
            ('onions by weight', 99, 500, 'g')
        ]
    ),
    (['milk'], False, False, 'L', {
            'cup': 1,
        }, [
            ('1L Tnuva', 1000, 1, 'L'),
            ('2L Tnuva', 1700, 2, 'L'),
            ('1L Tara', 1100, 1, 'L')
        ]
    ),
    (['salt'], True, False, 'g', {
            'teaspoon': 0.1,
            'tablespoon': 0.2
        }, [
            ('1 kg Sugat', 1000, 1000, 'g'),
            ('3kg Sugat', 2500, 3000, 'g')
        ]
    ),
    (['black pepper'], True, False, 'g', {
            'teaspoon': 0.1,
            'tablespoon': 0.2
        }, [
            ('100g ground black pepper', 500, 100, 'g')
        ]
    ),
    (['oregano'], True, False, 'g', {
            'teaspoon': 0.1,
            'tablespoon': 0.2
        }, [
            ('100g oregano', 500, 100, 'g')
        ]
    ),
    (['red pepper'], True, False, 'g', {
            'teaspoon': 0.1,
            'tablespoon': 0.2,
        }, [
            ('100g ground red pepper', 500, 100, 'g')
        ]
    ),
    (['pasta'], False, False, 'g', {}, [
            ('500g spaghetti', 1500, 500, 'g'),
            ('500g penne', 2000, 500, 'g')
        ]
    ),
    (['bacon'], False, True, 'g', {}, [
            ('bacon by weight', 100, 100, 'g'),
        ]
    ),
    (['celery'], False, True, 'g', {
        'single' : 300
        }, [
            ('celery by weight', 299, 500, 'g'),
        ]
    ),
    (['carrot', 'carrots'], False, True, 'g', {
        'single': 100
        }, [
            ('carrots by weight', 299, 500, 'g'),
        ]
    ),
    (['garlic'], False, True, 'g', {
        'clover' : 10,
        'clove' : 10,
        'single' : 1,
        "ml" : 0.25
        }, [
            ('single garlig head', 100, 100, 'g')
        ]
    ),
    (['butter'], True, False, 'g', {
        'single' : 500,
        'tablespoon': 0.1,
        'tablespoons': 0.1
        }, [
            ('500g butter Tnuva', 1000, 500, 'g'),
            ('500g butter TARA', 1000, 500, 'g')
        ]
    ),
    (['olive oil'], True, False, 'L', {
        'single' : 1000,
        'tablespoon': 0.1,
        'tablespoons': 0.1,
        'cup' : 100
        }, [
            ('1L olivia extra virgin olive oil', 1000, 1000, 'L'),
            ('1L el oilio extra virgin olive oil', 1200, 1000, 'L')
        ]
    ),
    (['ground beef'], False, True, 'g', {
        }, [
            ('ground beef', 500, 100, 'g')
        ]
    ),
    (['ground pork'], False, True, 'g', {
        }, [
            ('ground pork', 550, 100, 'g')
        ]
    ),
    (['beef consomme'], False, True, 'g', {
        'can': 800
        }, [
            ('beef consomme can', 1200, 800, 'g')
        ]
    ),
    (['white wine', 'dry white wine'], False, False, 'L', {
        'cup' : 0.2,
        'cups' : 0.2
        }, [
            ('1L white wine', 2000, 1, 'L')
        ]
    ),
    (['red wine', 'dry red wine'], False, False, 'L', {
        'cup' : 0.2,
        'cups' : 0.2
        }, [
            ('1L red wine', 2000, 1, 'L')
        ]
    ),
]

product = lambda b: {
    'name': b[0],
    'price': b[1],
    'min_amount': b[2],
    'unit': b[3]
}
food_type = lambda p: {
    'names': p[0],
    'starts_disabled': p[1],
    'sold_by_weight': p[2],
    'natural_unit': p[3],
    'conversions': p[4],
    'products': map(product, p[5])
}
products = map(food_type, food_type_data)

units =["g", "kg", "can", "cans", "liter", "L", "ml", "spoon", "spoons", "teaspoon", "teaspoons", "tablespoon", "tablespoons", "slices", "slice", "cup", "cups", "lb"]
ommitable =["sliced", "diced", "extra", "virgin", "sea", "fresh", "lean", "small", "medium", "large", "stalk"]


def parse(ingredients_list):
    output_list = []
    lines = ingredients_list.split("\n")
    for line in lines:
        pass
        output_list.append(get_product_details(line))
    return output_list


def get_price(product_list):
    pass


def get_product_details(line):
    omitted_words = []
    amount = 1.0
    unit = 'single'
    line = remove_parentheses(line)

    lines = line.split(' or ')
    for single_line in lines:
        words = single_line.split(" ")
        for word in words:
            if word_is_number(word):
                single_line = single_line.replace(word, "", 1)
                if word.find('-') != -1:
                    word = word.split('-')[1]
                if word.find('/') != -1:
                    numbers = word.split('/')
                    word = float(numbers[0])/int(numbers[1])
                amount = float(word)
                continue
            if word_is_unit(word):
                single_line = single_line.replace(word, "", 1)
                unit = word
                continue
            if word_is_ommitable(word):
                single_line = single_line.replace(word, "", 1)
                omitted_words.append(word)
                continue
            single_line = fix_spaces(single_line)

        details = {}
        details["products"] = []
        for food_type in products:
            for food in food_type["names"]:
                if food in single_line:
                    details["starts_disabled"] = food_type["starts_disabled"]
                    for product in food_type["products"]:
                        quantity = calc_quantity_per_product(product, unit, amount, food_type["conversions"])
                        if food_type["sold_by_weight"]:
                            details["products"].append({"name" : product["name"], "quantity" : quantity, "weight_unit": product["unit"],  'unit_weight': product["min_amount"]})
                        else:
                            details["products"].append({"name" : product["name"], "quantity" : quantity, "weight_unit": product["unit"]})

        if len(details["products"]) > 0:
            return details

    if len(details["products"]) == 0:
        print "error, didnt find product: " + line

    return details

def word_is_number(word):
    match = re.search("\d", word)
    if match:
        return True
    return False


def word_is_unit(word):
    if word in units:
        return True
    return False


def word_is_ommitable(word):
    if word in ommitable:
        return True
    return False


def fix_spaces(line):
    line = re.sub(' +', ' ', line)
    line = line.lstrip()
    return line.rstrip()

def remove_parentheses(line):
    start = line.find('(')
    end = line.find(')')
    if start == -1 and end == -1:
        return line
    word = line[start:end+1]
    return line.replace(word, "")

def calc_quantity_per_product(product, unit, amount, conversions):
    if unit in conversions:
        amount = conversions[unit] * amount
    else:
        amount = classic_conversion(unit, product["unit"], amount)
    quantity = int(amount / product["min_amount"])
    if amount % product["min_amount"]:
        quantity += 1;

    return quantity

def classic_conversion(recipe_unit, product_unit, amount):
    if recipe_unit == product_unit or recipe_unit == '':
        return amount
    if recipe_unit == 'kg' and product_unit == 'g':
        return amount * 1000
    if recipe_unit == 'g' and product_unit == 'kg':
        return float(amount) / 1000
    if recipe_unit == 'ml' and product_unit == 'L':
        return amount * 1000
    if recipe_unit == 'L' and product_unit == 'ml':
        return float(amount) / 1000
    if recipe_unit == 'lb' and product_unit == 'kg':
        return amount * 0.453592
    if recipe_unit == 'lb' and product_unit == 'g':
        return amount * 453.592
    if recipe_unit == 'ounce' and product_unit == 'ml':
        return amount * 29.5735
    if recipe_unit == 'ounce' and product_unit == 'L':
        return amount * 0.0295735
    print "UNITS ERROR FIX ME!!!!!!! recipe_unit = " + recipe_unit + " product_unit = " + product_unit

#print get_product_details('1 cup tomato sauce')
#print get_product_details('1 kg flour')
#print get_product_details('1 cup diced onions')
#print get_product_details('onion')
#print get_product_details('1 cup olive oil')



print get_product_details('1/4 lb bacon')
print get_product_details('1 medium onion (finely chopped)')
print get_product_details('1 stalk celery (finely chopped)')
print get_product_details('1 large carrot (finely chopped)')
print get_product_details('1 (2 teaspoon) jar garlic or 4 cloves garlic (minced)')
print get_product_details('4 tablespoons butter or 4 tablespoons margarine')
print get_product_details('3 tablespoons olive oil')
print get_product_details('1 lb lean ground beef')
print get_product_details('1/2-3/4 lb ground pork')
print get_product_details('1 (8 ounce) can beef consomme')
print get_product_details('1 cup dry white wine')
print get_product_details('1 (28 ounce) cans&w italian style crushed tomatoes (or other)')
print get_product_details('1 teaspoon salt')
print get_product_details('1/2 teaspoon black pepper')
print get_product_details('1 teaspoon rubbed sage')
print get_product_details('1 tablespoon oregano')
print get_product_details('1/2 teaspoon red pepper flakes')
print get_product_details('1/4 teaspoon nutmeg')
print get_product_details('1 cup milk (I use 2%)')
print get_product_details('1 lb small penne pasta')




#assert get_product_details('1 kg flour') == {'amount': '1', 'product': 'flour', 'unit': 'kg'}
#assert get_product_details('1 cup tomato sauce') == (1, 'kg', 'flour')
#assert get_product_details('1 cup diced onions') == {'amount': '1', 'product': 'onions', 'unit': 'cup'}
