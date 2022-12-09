from person import Person
from book import Book

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
      self.catalog.append(Book(clean_line[1],clean_line[0]))

  def __repr__(self):
    return "; ".join([self.name] + [repr(b) for b in self.catalog])

  def __add__(self, other):
    if isinstance(other, Book):
      if other not in self.catalog:
        self.catalog.append(other)
      else:
        print(f"{other.title} already in library")
    else:
      print(f"{type(other)} cannot be added to a library.")
    return self

  def __sub__(self, other):
    if isinstance(other, Book):
      if other in self.catalog and other.status:
        self.catalog.remove(other)
      elif not other.status:
        print(f"{other.title} unavailable")
      else:
        print(f"{other.title} not in library")
    else:
      print(f"{type(other)} cannot be removed from a library.")
    return self

  def __len__(self):
    return len(self.catalog)

  def __str__(self):
    return self.name

  def print_catalog(self):
    for b in self.catalog:
      print(f"{b.title}: {b.full_status()}")

  def print_available(self):
    for b in self.catalog:
      if b.status:
        print(b.title)

  def print_unavailable(self):
    for b in self.catalog:
      if not b.status:
        print(b.full_status())

  def checkout(self, book, person, debug = False):
    if debug:
      print(f"{person} checking out {book}")
    if isinstance(book, Book):
      if book in self.catalog and book.status:
        book.status = False
        book.currentPerson = person
        person.books.append(book.title)
      elif book not in self.catalog:
        print(f"{book.title} not in library")
      else:
        print(f"{book.title} already checked out")
    else:
      print(f"{type(book)} cannot be removed from a library.")

  def turn_in(self, book, person, debug = False):
    if debug:
      print(f"{person} turning in {book}")
    if isinstance(book, Book):
      if book in self.catalog and book.currentPerson is person:
        book.status = True
        if person not in book.pastPeople:
          book.pastPeople.append(person)
        book.currentPerson = None
        person.books.remove(book.title)
      elif book not in self.catalog:
        print(f"{book.title} not in library")
      else:
        print(f"{person} does not have the book.")
    else:
      print(f"{type(book)} cannot be removed from a library.")