class Person:
  def __init__(self, firstName, lastName):
    self.firstName = firstName
    self.lastName = lastName
    self.books = []

  def __repr__(self):
    return ", ".join([f"{self.firstName} {self.lastName}"] + self.books)

  def __len__(self):
    return len(self.books)

  def __str__(self):
    return f"{self.firstName} {self.lastName}"

  def print_name(self):
    print(self.firstName, self.lastName)

  def print_current_books(self):
    print(self.books)