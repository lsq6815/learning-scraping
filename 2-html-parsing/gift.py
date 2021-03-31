#!/usr/bin/env python3
"""
Gift.py: define Gift class
"""


class Gift():
    """
    class to expression gift
    """

    def __init__(self, name: str, desc: str, price: float):
        """init object

        init the object with name, desc, price

        Args:
            name: name of gift 
            desc: gift description
            price: price of gift
        """
        self.name = name
        self.desc = desc
        self.price = price

    def __str__(self):
        """toString

        return Gift as string
        """
        return f"Name: {self.name.title()}\nPrice: {self.price}\nDescription:\n{self.desc}\n"
