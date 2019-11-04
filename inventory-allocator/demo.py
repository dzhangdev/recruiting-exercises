#
# Inventory Allocation (Python 3)
#
# Run this command-line program with no arguments.
#
# Qixiang Zhang (David)
# qixianz@uci.edu
# https://www.linkedin.com/in/dzhangdev
#


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
    Output: [{ owd: { apple: 1 } }]
    Explanation: Happy Case, exact inventory match!
    """
    pass


def do_basic_not_enough_inventory_test():
    """ Creates a not enough inventory case, and prints the result to the console
    Example 1:
    Input: { apple: 1 }, [{ name: owd, inventory: { apple: 0 } }]
    Output: []
    Explanation: Not enough inventory -> no allocations!
    """
    pass


def do_basic_split_test():
    """ Creates a not enough inventory case, and prints the result to the console
    Example 1:
    Input: { apple: 10 },
            [{ name: owd, inventory: { apple: 5 } },
             { name: dm,  inventory: { apple: 5 }}]
    Output: [{ dm: { apple: 5 }}, { owd: { apple: 5 } }]
    Explanation: Should split an item across warehouses if that is the only way to completely ship an item!
    """
    pass


def do_random_test():
    """ Randomly creates 1000 cases, and prints the results to the console """
    pass


# Run the main program
if __name__ == "__main__":
    main()
