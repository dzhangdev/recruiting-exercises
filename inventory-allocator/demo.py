#
# Inventory Allocation (Python 3)
#
# Run this command-line program with no arguments.
#
# Qixiang Zhang (David)
# qixianz@uci.edu
# https://www.linkedin.com/in/dzhangdev
#

from src.InventoryAllocator import InventoryAllocator
from src import util


def main():
    """Run all test cases here"""
    do_basic_happy_test()
    do_basic_not_enough_inventory_test()
    do_basic_split_test()
    do_random_test()


# --------- Demo tests -----------

def do_basic_happy_test():
    """ Creates a happy exact match case, and prints the result to the console
    Example:
    Input: { apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]
    Output: [{'owd': {'apple': 1}}]
    Explanation: Happy Case, exact inventory match!
    """
    order = {'apple' : 1}
    warehouse_inventories = [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]
    allocation = InventoryAllocator.allocate(order, warehouse_inventories)

    answer = "[{'owd': {'apple': 1}}]"
    print("{} the basic happy test!".format('Passed' if str(allocation) == answer else 'failed'))


def do_basic_not_enough_inventory_test():
    """ Creates a not enough inventory case, and prints the result to the console
    Example 1:
    Input: { apple: 1 }, [{ name: owd, inventory: { apple: 0 } }]
    Output: []
    Explanation: Not enough inventory -> no allocations!
    """
    order = {'apple' : 1}
    warehouse_inventories = [{ 'name': 'owd', 'inventory': { 'apple': 0 } }]
    allocation = InventoryAllocator.allocate(order, warehouse_inventories)

    answer = "[]"
    print("{} the basic not enough inventory test!".format('Passed' if str(allocation) == answer else 'failed'))


def do_basic_split_test():
    """ Creates a not enough inventory case, and prints the result to the console
    Example 1:
    Input: { apple: 10 },
            [{ name: owd, inventory: { apple: 5 } },
             { name: dm,  inventory: { apple: 5 }}]
    Output: [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
    Explanation: Should split an item across warehouses if that is the only way to completely ship an item!
    """
    order = {'apple' : 1}
    warehouse_inventories = [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm',  'inventory': { 'apple': 5 }}]
    allocation = InventoryAllocator.allocate(order, warehouse_inventories)

    answer = "[{'owd': {'apple': 1}}, {'dm': {'apple': 1}}]"
    print("{} the basic split test!".format('Passed' if str(allocation) == answer else 'failed'))


def do_random_test():
    """ Randomly creates 1000 cases, and prints the results to the console """
    NUM_TESTS = 1000
    for _ in range(NUM_TESTS):
        order = util.generate_order()
        warehouse_inventories = util.generate_warehouses()
        allocation = InventoryAllocator.allocate(order, warehouse_inventories)
        print(str(allocation))


# Run the main program
if __name__ == "__main__":
    main()
