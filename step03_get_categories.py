import json

def add_categories_to_data(data):
    for i in range(len(data)):
        if 0 <= i <= 39:
            data[i]['cat'] = 'dairy'
        elif 40 <= i <= 71:
            data[i]['cat'] = 'plant-based'
        elif 72 <= i <= 127:
            data[i]['cat'] = 'additives'
        elif 128 <= i <= 130:
            data[i]['cat'] = 'fmcg-en'
        else:
            data[i]['cat'] = 'other/category-3'
    return data

def write_data_to_file(file_path, data):
    with open(file_path, 'w', encoding="utf-8") as json_file:
        json.dump(data, json_file)

def process_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as json_file:
        data = json.load(json_file)
    data = add_categories_to_data(data)
    write_data_to_file(file_path, data)

# call the function with the path to your json file
process_file('data/short_desc_products.json')
