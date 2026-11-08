#!/usr/bin/env python3


class Book:
    """Represent a book that can be read one page at a time."""

    def __init__(self, title, page_count):
        """Create a book with a title and a number of pages."""
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        """Return the number of pages in the book."""
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        """Only allow the page count to be stored as an integer."""
        if isinstance(value, int) and not isinstance(value, bool):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """Tell the reader that the book's page is being turned."""
        print("Flipping the page...wow, you read fast!")
        
