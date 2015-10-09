import re

__author__ = 'eitanz'
food_type_data = [
    (['tomato', 'tomatoes', 'fresh tomatoes'], False, True, 'g', {
            'cup': 200,
            'unitless' : 150
        }, [
            ('tomatoes by weight', 99, 500, 'g')
        ]
    ),
    (['crushed tomatoes', 'tomato sauce', 'tomatoes sauce', 'fresh tomatoes sauce'], False, False, 'g', {
        'cup': 300,
        'unitless':200
        }, [
            ('100g osem tomato sauce', 120, 100, 'g'),
            ('200g osem tomato sauce', 200, 200, 'g')
        ]
    ),
    (['egg', 'eggs'], False, False, 'unitless', {}, [
            ('6 pack free range eggs', 1500, 6, 'unitless'),
            ('12 pack free range eggs', 2000, 12, 'unitless'),
            ('6 pack eggs', 1000, 6, 'unitless'),
            ('12 pack eggs', 1600, 12, 'unitless')
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
            'unitless' : 150
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
    (['sage'], True, False, 'g', {
            'teaspoon': 0.1,
            'tablespoon': 0.2
        }, [
            ('100g sage', 500, 100, 'g')
        ]
    ),
    (['nutmeg'], True, False, 'g', {
            'teaspoon': 0.1,
            'tablespoon': 0.2
        }, [
            ('100g nutmeg', 500, 100, 'g')
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
        'unitless' : 300
        }, [
            ('celery by weight', 299, 500, 'g'),
        ]
    ),
    (['carrot', 'carrots'], False, True, 'g', {
        'unitless': 100
        }, [
            ('carrots by weight', 299, 500, 'g'),
        ]
    ),
    (['garlic'], False, True, 'g', {
        'clover' : 10,
        'clove' : 10,
        'unitless' : 1,
        }, [
            ('single garlic head', 100, 100, 'g')
        ]
    ),
        (['jar garlic', 'garlic jar'], False, False, 'g', {
        'unitless' : 1,
        "ml" : 0.25
        }, [
            ('single garlic jar', 100, 550, 'g')
        ]
    ),
    (['butter'], True, False, 'g', {
        'unitless' : 500,
        'tablespoon': 0.1,
        'tablespoons': 0.1
        }, [
            ('500g butter Tnuva', 1000, 500, 'g'),
            ('500g butter TARA', 1000, 500, 'g')
        ]
    ),
    (['olive oil'], True, False, 'L', {
        'unitless' : 1000,
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
food_types = map(food_type, food_type_data)

units =["g", "kg", "can", "cans", "liter", "L", "ml", "spoon", "spoons", "teaspoon", "teaspoons", "tablespoon", "tablespoons", "slices", "slice", "cup", "cups", "lb"]
ommitable =["", "sliced", "diced", "extra", "virgin", "sea", "fresh", "lean", "small", "medium", "large", "stalk", "cans&w", "italian", "style", "rubbed", "flakes", "penne"]


class NoSuchFoodType(Exception): pass

def parse(ingredients_list):
    ingredients_started = False
    ingredients_ended = False
    output_list = []
    lines = ingredients_list.split("\n")
    for line in lines:
        pass
        if line != '':
            try:
                output_list.append(get_product_details(line))
                if not ingredients_started:
                    ingredients_started = True
                if ingredients_ended:
                    raise NoSuchFoodType("LAST LINE")
            except NoSuchFoodType:
                if ingredients_started:
                    ingredients_ended = True
                    #raise

    return output_list


def get_price(product_list):
    price = 0
    for product in product_list:
        for food_type in food_types:
            for db_product in food_type['products']:
                if product["brand"] == db_product["name"]:
                    price += product["quantity"] * db_product["price"]
                    break
    return price
assert get_price([{"brand" : '200g osem tomato sauce', "quantity" : 2}, {"brand" : '1L white wine', "quantity" : 3}]) == 6400



def get_product_details(line):
    line = remove_parentheses(line)
    first_option = line.split(' or ')[0]
    return get_single_product_details(first_option)

def get_single_product_details(line):
    amount, unit, product_name = separate_product_details(line)

    for food_type in food_types:
        if product_name in food_type["names"]:
            return {
                "starts_disabled": food_type["starts_disabled"],
                "products": get_food_type_products(food_type, amount, unit)
            }
    raise NoSuchFoodType("didn't find food type: " + line)

def word_contains_digit(word):
    match = re.search("\d", word)
    return bool(match)
assert word_contains_digit('asdf5fasdf')
assert not word_contains_digit('asdffasdf')

def word_is_unit(word):
    return word in units

def word_is_ommitable(word):
    return word in ommitable

def parse_amount(word):
    if word.find('-') != -1:
        low, high = word.split('-')
        word = high

    if word.find('/') != -1:
        a, b = word.split('/')
        return float(a) / int(b)
    else:
        return float(word)
assert parse_amount('0') == 0.0
assert parse_amount('12') == 12.0
assert parse_amount('3/4') == 0.75
assert parse_amount('2-6') == 6.0
assert parse_amount('1/2-2') == 2.0
assert parse_amount('1/2-3/4') == 0.75

def remove_parentheses(line):
    if re.search(r'\([^)]*\(', line):
        raise ValueError()
    return re.sub(r'\([^)]*\)', '', line)
assert remove_parentheses('a(b)c(d)e') == 'ace'
try:
    remove_parentheses('(())')
    assert False
except ValueError:
    pass

def separate_product_details(line):
    amount = 1.0
    unit = 'unitless'

    words = line.split(" ")
    product_words = []
    for i in xrange(len(words)):
        word = words[i]
        if word_is_unit(word):
            assert unit == 'unitless'
            unit = word
        elif word_is_ommitable(word):
            pass
        elif word_contains_digit(word):
            amount = parse_amount(word)
        else:
            product_words.append(word)

    product_name = ' '.join(product_words)
    return amount, unit, product_name
assert separate_product_details('onion') == (1, 'unitless', 'onion')
assert separate_product_details('250 g bacon') == (250.0, 'g', 'bacon')
assert separate_product_details('1/4 kg bacon') == (0.25, 'kg', 'bacon')
assert separate_product_details('1 jar garlic') == (1, 'unitless', 'jar garlic')

CONVERSIONS = {
    ('kg', 'g'): 1000.0,
    ('g', 'kg'): 0.001,
    ('lb', 'kg'): 0.453592,
    ('lb', 'g'): 453.592,
    ('ml', 'L'): 0.001,
    ('L', 'ml'): 1000.0,
    ('ounce', 'ml'): 29.5735,
    ('ounce', 'L'): 0.0295735,
}
def classic_conversion(from_unit, to_unit, amount):
    if from_unit == to_unit:
        return amount
    key = (from_unit, to_unit)
    if key in CONVERSIONS:
        return amount * CONVERSIONS[key]

    raise ValueError("UNITS ERROR FIX ME!!!!!!! recipe_unit = " + from_unit + " product_unit = " + to_unit)
assert classic_conversion('kg', 'g', 10) == 10000
assert classic_conversion('ml', 'L', 10) == 0.01

def calc_quantity_per_product(product, unit, amount, conversions):
    if unit in conversions:
        amount = conversions[unit] * amount
    else:
        amount = classic_conversion(unit, product["unit"], amount)
    quantity = int(amount / product["min_amount"])
    if amount % product["min_amount"]:
        quantity += 1;

    return quantity
_onion = product(('onion', 50, 1, 'unitless'))
_bacon = product(('bacon by weight', 100, 100, 'g'))
assert calc_quantity_per_product(_onion, 'kg', 0.2, {'kg': 20.0}) == 4
assert calc_quantity_per_product(_bacon, 'g', 250.0, {}) == 3
assert calc_quantity_per_product(_bacon, 'kg', 0.25, {}) == 3

def get_food_type_products(food_type, amount, unit):
    products = []
    for product in food_type["products"]:
        
        products.append({
            "name" : product["name"],
            "quantity": calc_quantity_per_product(product, unit, amount, food_type["conversions"]),
            "price": product["price"],
            "weight_unit": product["unit"] if food_type["sold_by_weight"] else None,
            "unit_weight": product["min_amount"] if food_type["sold_by_weight"] else None
        })
    return products

_eggs_index = 0
while 'eggs' not in food_types[_eggs_index]['names']:
    _eggs_index += 1
_egg_products = get_food_type_products(food_types[_eggs_index], 3, 'unitless')
assert [p['name'] for p in _egg_products] == ['6 pack free range eggs', '12 pack free range eggs', '6 pack eggs', '12 pack eggs']
assert _egg_products[0] == {'name': '6 pack free range eggs', 'price': 1500, 'quantity': 1, 'unit_weight': None, 'weight_unit': None}
assert _egg_products[-1] == {'name': '12 pack eggs', 'price': 1600, 'quantity': 1, 'unit_weight': None, 'weight_unit': None}
_egg_products = get_food_type_products(food_types[_eggs_index], 10, 'unitless')
assert [p['name'] for p in _egg_products] == ['6 pack free range eggs', '12 pack free range eggs', '6 pack eggs', '12 pack eggs']
assert _egg_products[0] == {'name': '6 pack free range eggs', 'price': 1500, 'quantity': 2, 'unit_weight': None, 'weight_unit': None}
assert _egg_products[-1] == {'name': '12 pack eggs', 'price': 1600, 'quantity': 1, 'unit_weight': None, 'weight_unit': None}

assert get_product_details('1 cup tomato sauce')['products'][0]['name'] == '100g osem tomato sauce'

_recipe = '''
Blah blah

1/4 lb bacon
1 medium onion (finely chopped)
1 stalk celery (finely chopped)
1 large carrot (finely chopped)
1 (2 teaspoon) jar garlic or 4 cloves garlic (minced)
4 tablespoons butter or 4 tablespoons margarine
3 tablespoons olive oil
1 lb lean ground beef
1/2-3/4 lb ground pork
1 (8 ounce) can beef consomme
1 cup dry white wine
1 (28 ounce) cans&w italian style crushed tomatoes (or other)
1 teaspoon salt
1/2 teaspoon black pepper
1 teaspoon rubbed sage
1 tablespoon oregano
1/2 teaspoon red pepper flakes
1/4 teaspoon nutmeg
1 cup milk (I use 2%)
1 lb small penne pasta

blah blah
'''
assert len(parse(_recipe)) == 20
