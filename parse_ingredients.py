import re

__author__ = 'eitanz'

products = ["tomato sauce", "tomatoes", "eggs", "olive", "olive oil"]
units = ["g", "kg", "can", "cans", "liter", "L", "spoon", "spoons", "tablespoon", "tablespoons", "slices", "slice", "small", "large"]
ommitable = ["sliced", "diced", "extra", "virgin", "ground", "sea", "cup"]
def parse(ingredients_list):
    output_list = list
    lines = ingredients_list.split("\n")
    for line in lines:
        output_list.append(get_product_details(line))
    return output_list





def get_price(product_list):
    pass

def get_product_details(line):
    details = dict
    words = line.split(" ")
    omitted_words = list
    for word in words:
        if word_is_number(word):
            details["amount"] = word
            line = line.replace(word, "", 1)
            continue
        if word_is_unit(word):
            details["unit"] = word
            line = line.replace(word, "", 1)
            continue
        if word_is_ommitable(word):
            omitted_words.append(word)
            line = line.replace(word, "", 1)
            continue
    if line in products:
        details["product"] = line
    else:
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

assert get_product_details('1 kg flour') == (1, 'kg', 'flour')
# assert get_product_details('1kg flour') == (1, 'kg', 'flour')
assert get_product_details('1 cup diced onions') == (1, 'cup', 'onion')
