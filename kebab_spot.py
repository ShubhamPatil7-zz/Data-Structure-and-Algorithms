__author__ = 'IAV'
__author__ = 'SBP'
"""
A module that represents "spots" on the skewer.

Author: Sean Strout @ RITCS
Author: Indrajeet Vidhate
Author: Shubham Patil
"""


class KebabSpot:
    """
    Class: KebabSpot
    Description: This class is used to represent an individual
        spot on the skewer.  Each spot contains a food item,
        and a reference to the next spot.  
    """

    __slots__ = ['item', 'next', 'total_size']

    def __init__(self, item, next):
        """
        Construct a KebabSpot instance.
        :param item: the item (Food) to store at this spot
        :param next: the next KebabSpot on the skewer
        """
        self.next = next
        self.item = item
        pass

    def size(self):
        """
        Return the number of elements from this KebabSpot instance to the end
        of the skewer.
        :return: the number of elements (int)
        """
        self.total_size = 0
        current = self

        while (current != None):
            self.total_size += 1

            current = current.next

        return self.total_size

    def is_vegan(self):
        """
        Return whether there are all vegetables from this spot to the end of
        the skewer.
        :return True if there are no vegetables from this spot down, 
        False otherwise.

        """
        current = self
        while (current != None):
            if (not current.item.is_veggie):
                return False
            current = current.next

        return True

    def calories(self):
        """
        This method returns summation of calories of all the food
        items currently present on the skewer.
        :return: total calories on skewer
        """
        current = self
        calories = 0
        while current != None:
            calories += current.item.calories
            current = current.next
        return calories

    def has(self, name):
        """
        Return whether there are any vegetable from this spot to the end of
        the skewer.
        :param name: the name (string) being searched for.
        :return True if any of the spots hold a Food item that equals the
        name, False otherwise.
        """
        current = self
        while current != None:
            if current.item.name == name:
                return True
            current = current.next

        return False

    def string_em(self):
        """
        Return a string that contains the list of items in the skewer from
        this spot down, with a comma after each entry.
        :return A string containing the names of each of the Food items from
        this spot down.
        """
        current = self
        names = ""
        while current != None:
            if current.next == None:
                names += current.item.name
            else:
                names += current.item.name + ','
            current = current.next
        return names

    def get_item(self):
        return self.item
