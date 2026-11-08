#!/usr/bin/env python3


class Coffee:
    """Represent a coffee drink sold by the bookstore."""

    def __init__(self, size, price):
        """Create a coffee with a size and a price."""
        self.size = size
        self.price = price

    @property
    def size(self):
        """Return the coffee's size."""
        return self._size

    @size.setter
    def size(self, value):
        """Only allow Small, Medium, or Large coffee sizes."""
        if value in ("Small", "Medium", "Large"):
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        """Print a thank-you message and add one dollar to the price."""
        print("This coffee is great, here’s a tip!")
        self.price += 1
