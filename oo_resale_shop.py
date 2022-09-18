from typing import Dict, Union, Optional
import computer

class ResaleShop:
    
    def __init__(self):
        self.inventory : Dict[int, computer.Computer] = {}

    """
    Takes in a Dict containing all the information about a computer,
    adds it to the inventory, returns the assigned item_id
    """
    def buy(self, newComputerInfo: Dict[str, Union[str, int, bool]]):
        newComputer: computer.Computer = computer.Computer(newComputerInfo)
        self.inventory[newComputer.getID()] = newComputer
        return newComputer.getID()
            
    """
    Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")
    
    """
    prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")

    def getComputer(self, itemID:int):
        return self.inventory[itemID]
    

