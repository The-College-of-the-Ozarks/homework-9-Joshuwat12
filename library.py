import book as b

class Library:
    # __init__
    # Requires catalog to be a file OPEN FOR READING
    # The catalog file has columns author and title
    # Currently this requires the Book class to be defined
    # in a file called book.py (you may change these as desired)
    # and requires the Book class __init__() function to take
    # the title of the book first, author second.
    def __init__(self, name, catalog):
        self.name = name
        self.catalog = []
        for line in catalog:
            clean_line = line.strip()
            clean_line = clean_line.split(',')
            self.catalog.append(b.Book(clean_line[1],clean_line[0]))