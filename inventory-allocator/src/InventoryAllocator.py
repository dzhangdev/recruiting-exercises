#
# Inventory Allocation (Python 3)
#
# InventoryAllocator Class Defination
#
# Qixiang Zhang (David)
# qixianz@uci.edu
# https://www.linkedin.com/in/dzhangdev


from collections import OrderedDict


class InventoryAllocator(object):
    """ Inventory allocator takes in the order and pre-sorted inventory list,
    and return the allocation map. Inventory allocator uses greedy algorithm
    since the input inventory is pre-sorted per cost.
    """
    @staticmethod
    def allocate(order, warehouse_inventories):
        """ Allocate inventories per order from available warehouses using
        greedy algorithm

        Parameters
        ----------
        order: None or dict()
            Input data. Note that order can be empty or None. In both cases
            should return []

        warehouse_inventories: None or list(dict(dict))
            Input data. Note that the warehouse inventories can be None or
            empty. In both cases should return [].

            Each warehouse dict contains 'name' and 'inventory' keys. For value
            for 'name', I assume it is not empty and unique per problem
            assumption. For the 'inventory' values, it is a dict type contains
            available inventories.

        Returns
        -------
        allocation: list(dict)
            Output data. Note that it can be empty, or contain 1 or more dict
            type allocation among available warehouses.
        """
        # return empty list if None or empty input data
        if (not order or not warehouse_inventories):
            return []

        # keep the warehouse filling order sorted
        allocation_map = OrderedDict()

        # iterate through the warehouses from the cheapest to the most expensive
        for warehouse_map in warehouse_inventories:

            # if the order is filled, return the allocation
            if not order:
                break

            # iterate through remaining orders
            for product in order:

                # check if the warehosue has the item in the inventory
                if (product in warehouse_map['inventory'] and warehouse_map['inventory'][product] > 0):

                    # allocate the max possible
                    allocate_amount = min(warehouse_map['inventory'][product], order[product])

                    # mark the warehouse if not present
                    if warehouse_map['name'] not in allocation_map:
                        allocation_map[warehouse_map['name']] = dict()

                    # put the inventory in the allocation order
                    allocation_map[warehouse_map['name']][product] = allocate_amount

                    # remove item from order if the remaining required amount is 0
                    if(order[product] == 0):
                        del order[product]

        return [{key: value} for key, value in allocation_map.items()]
