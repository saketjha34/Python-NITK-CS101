"""
Inventory management
using dictionaries
"""

def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    dict = {}
    for i in range(len(items)):
        dict[items[i]] = items.count(items[i])
    return dict

def add_items(inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    for i in items:
        inventory[i] = inventory.get(i, 0) + 1
    return inventory


def decrement_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """
    for i in items:
        if i in inventory and inventory[i]>0:
            inventory[i] = inventory.get(i, 0) - 1
    return inventory

def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    if item in inventory:
        del inventory[item]
    return inventory
print(remove_item({"coal":2, "wood":1, "diamond":2}, "gold"))

def list_inventory(inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    return [(i,j) for i, j in inventory.items() if j>0]