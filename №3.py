import yaml

info = {'books_name': ['book_1', 'book_2', 'book_3'],
        'books_num': 3,
        'books_price': {'book_1': '100€',
                       'book_2': '200₽',
                       'book_3': '300¥'}
        }

with open('file.yaml', 'w', encoding='utf-8') as writing:
    yaml.dump(info, writing, default_flow_style=False, allow_unicode=True)

with open("file.yaml", 'r', encoding='utf-8') as reading:
    get_info = yaml.load(reading)

print(info == get_info)