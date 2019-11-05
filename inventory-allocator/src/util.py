#
# Utility for generating random test cases (Python 3)
#
# Qixiang Zhang (David)
# qixianz@uci.edu
# https://www.linkedin.com/in/dzhangdev


import random


PRODUCTS = [
    'apple',
    'banana',
    'chicken',
    'dragonfruit',
    'egg',
    'fajita',
    'granola',
    'hummus',
    'icecream',
    'jalapeno',
]

TOTAL_NUM_PRODUCTS = len(PRODUCTS)

ORDER_MAX_QUANTITY = 5

MAX_NUM_WAREHOUSES = 10 # TOTAL_NUM_PRODUCTS * ORDER_MAX_QUANTITY
MAX_WAREHOUSE_PRODUCT_COUNT = ORDER_MAX_QUANTITY * 2

WAREHOUSE_PREFIX = 'WareHouse_'

def generate_order(order_quantity=ORDER_MAX_QUANTITY):
    """ Generates a list of products with quantity """
    order = dict()
    num_products = random.randint(0, TOTAL_NUM_PRODUCTS + 1)
    for _ in range(num_products):
        item = PRODUCTS[random.randint(0, TOTAL_NUM_PRODUCTS - 1)]
        quantity = random.randint(0, order_quantity)
        order[item] = quantity if item not in order else quantity + order[item]
    return order

def generate_warehouses():
    """ Generate a list of warehouse with dictionary of inventories """
    warehouses = []
    num_warehouses = random.randint(0, MAX_NUM_WAREHOUSES)
    for i in range(num_warehouses):
        name = "{}{}".format(WAREHOUSE_PREFIX, i)
        inventory = generate_order(MAX_WAREHOUSE_PRODUCT_COUNT)
        warehouses.append({'name':name, 'inventory':inventory})
    return warehouses
