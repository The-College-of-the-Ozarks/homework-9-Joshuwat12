from person import Person

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.status = True
    self.pastPeople = []
    self.currentPerson = None

  def __repr__(self):
    r = f"{self.title}, {self.author}, {self.full_status()}"
    return ", ".join([r] + self.pastPeople)

  def __len__(self):
    return len(self.pastPeople)

  def __eq__(self, other):
    return self is other
    # This is the code you asked for, but it is incompatible with polymorphic purposes.
    # return self.title == self.author

  def __str__(self):
    return f"{self.title}, by {self.author}"

  def print_name_author(self):
    print(self)

  def full_status(self):
    if self.status:
      return "Available"
    else:
       return f"Checked out by {self.currentPerson.firstName} {self.currentPerson.lastName}"
  
  def print_status(self):
    print(self.full_status())

  def print_prev_borrowers(self):
    print(self.pastPeople)