#
# Inventory Allocation (Python 3)
#
# InventoryAllocator Class Defination
#
# Qixiang Zhang (David)
# qixianz@uci.edu
# https://www.linkedin.com/in/dzhangdev
#



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
        pass
