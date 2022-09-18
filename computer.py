from typing import Dict, Union, Optional

class Computer:
    
    itemID = 0

    def __init__(self, info : Dict[str, Union[str, int, bool]] = {}):
        Computer.itemID += 1
        self.__itemID = Computer.itemID
        self.__info : Dict[str, Union[str, int, bool]] = info

    """
    
    """
    def update_price(self, new_price: int):
        self.__info["price"] = new_price

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

    def getID(self):
        return self.__itemID

    def getInfo(self):
        return self.__info

    def __str__(self):
        return str(self.__info)