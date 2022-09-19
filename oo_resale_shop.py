from typing import Dict, Union, Optional
import computer
"""
ResaleShop class that can create instances of ResaleShop with their own inventories (dictionaries of computer info); 
Can also buy computers, sell computers, and print the current inventory
"""
class ResaleShop:
    """
    Constructor: creates instances of ResaleShop with inventory variable
    """
    def __init__(self, inventory: Dict[int, computer.Computer] = {}):
        self.__inventory = inventory # dictionary that relates computer ID to computer info

    """
    Getter method for inventory variable
    """
    def getInventory(self):
        return self.__inventory

    """
    Takes in a Dict containing all the information about a computer,
    adds computer to the inventory, returns the assigned item_id
    """
    def buy(self, newComputerInfo: Dict[str, Union[str, int, bool]]):
        newComputer: computer.Computer = computer.Computer(newComputerInfo)
        self.getInventory()[newComputer.getID()] = newComputer
        return newComputer.getID()
            
    """
    Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, item_id: int):
        if item_id in self.getInventory():
            del self.getInventory()[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")
    
    """
    Prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    def print_inventory(self):
        # If the inventory is not empty
        if self.getInventory():
            # For each item
            for item_id in self.getInventory():
                # Print its details
                print(f'Item ID: {item_id} : {self.getInventory()[item_id]}')
        else:
            print("No inventory to display.")

    """
    Returns a computer object given its ID
    """
    def getComputer(self, itemID:int):
        return self.getInventory()[itemID]