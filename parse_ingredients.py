import re

__author__ = 'eitanz'
food_type_data = [
    (['tomato', 'tomatoes', 'fresh tomatoes'], False, True, 'gr', {
            'cup': 200,
            'single' : 150
        }, [
            ('tomatoes by weight', 99, 500, 'gr')
        ]
    ),
    (['tomato sauce', 'tomatoes sauce', 'fresh tomatoes sauce'], False, False, 'gr', {
        'cup': 300
        }, [
            ('100g osem tomato paste', 120, 100, 'gr'),
            ('200g osem tomato paste', 200, 200, 'gr')
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
    (['onion', 'onions'], False, True, 'gr', {
            'cup': 200,
            'single' : 150
        }, [
            ('onions by weight', 99, 500, 'gr')
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

units =["g", "kg", "can", "cans", "liter", "L", "spoon", "spoons", "tablespoon", "tablespoons", "slices", "slice", "small", "large", "cup", "cups"]
ommitable =["sliced", "diced", "extra", "virgin", "ground", "sea", "fresh"]


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
    details = {}
    details["products"] = []
    words = line.split(" ")
    omitted_words = []
    amount = 1.0
    unit = 'single'
    for word in words:
        if word_is_number(word):
            amount = float(word)
            line = line.replace(word, "", 1)
            continue
        if word_is_unit(word):
            unit = word
            line = line.replace(word, "", 1)
            continue
        if word_is_ommitable(word):
            omitted_words.append(word)
            line = line.replace(word, "", 1)
            continue
    line = fix_spaces(line)
    for food_type in products:
        if line in food_type["names"]:
            details["starts_disabled"] = food_type["starts_disabled"]
            for product in food_type["products"]:
                quantity = calc_quantity_per_product(product, unit, amount, food_type["conversions"])
                if food_type["sold_by_weight"]:
                    details["products"].append({"name" : product["name"], "quantity" : quantity, "weight_unit": product["unit"],  'unit_weight': product["min_amount"]})
                else:
                    details["products"].append({"name" : product["name"], "quantity" : quantity, "weight_unit": product["unit"]})

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
    return line.lstrip()

def calc_quantity_per_product(product, unit, amount, conversions):
    print amount
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
    print "UNITS ERROR FIX ME!!!!!!! recipe_unit = " + recipe_unit + " product_unit = " + product_unit

print get_product_details('1 cup tomato sauce')
print get_product_details('1 kg flour')
print get_product_details('1 cup diced onions')
print get_product_details('onion')
print get_product_details('5 tomatoes')

#assert get_product_details('1 kg flour') == {'amount': '1', 'product': 'flour', 'unit': 'kg'}
#assert get_product_details('1 cup tomato sauce') == (1, 'kg', 'flour')
#assert get_product_details('1 cup diced onions') == {'amount': '1', 'product': 'onions', 'unit': 'cup'}
