from typing import Dict, Union, Optional

""" 
Computer class that can create instances of Computer with itemID (ID number) and info (dictionary containing computer info)
variables; can also update the price of a specific computer or refurbish it
"""
class Computer:
    
    itemID = 0 # ID number of computer instance created

    """
    Constructor: creates Computer object with itemID and info variables; itemID keeps track of how many computers created 
    (IDs taken) and uses the next number
    """
    def __init__(self, info : Dict[str, Union[str, int, bool]] = {}):
        Computer.itemID += 1
        self.__itemID = Computer.itemID
        self.__info : Dict[str, Union[str, int, bool]] = info

    """
    update_price method simply updates the price of a Computer object using the info variable
    """
    def update_price(self, new_price: int):
        self.__info["price"] = new_price

    """
    refurbish method reassigns the price of a computer based on its year made, and also assigns a new operating system 
    if one is given
    """
    def refurbish(self, new_os: Optional[str] = None):
        computer = self.__info
        if int(computer["year_made"]) < 2000:
            computer["price"] = 0 # too old to sell, donation only
        elif int(computer["year_made"]) < 2012:
            computer["price"] = 250 # heavily-discounted price on machines 10+ years old
        elif int(computer["year_made"]) < 2018:
            computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
        else:
            computer["price"] = 1000 # recent stuff
        if new_os is not None:
            computer["operating_system"] = new_os # update details after installing new OS

    """
    Getter method for itemID
    """
    def getID(self):
        return self.__itemID

    """
    Getter method for info dictionary
    """
    def getInfo(self):
        return self.__info

    """
    str method allows Computer object to be printed as its info dictionary
    """
    def __str__(self):
        return str(self.__info)