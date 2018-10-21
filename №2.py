import json


def write_order_to_json(item, quantity, price, buyer, date):

    with open('orders.json', 'r') as reading:
        info = json.load(reading)

    with open('orders.json', 'w') as writing:
        orders_list = info['orders']
        order_info = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
        orders_list.append(order_info)
        json.dump(info, writing, indent=4)


write_order_to_json('Magic stick', '1', '123456', 'Lord Volandemort', '31.01.1915')