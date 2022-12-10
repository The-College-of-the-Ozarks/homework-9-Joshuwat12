from person import Person
from book import Book
from library import Library
import random

# Function
def Divider():
  print("-" * 20)

# Library creation
catalog = open("catalog.csv", "r")
l = Library("Ross Boss Library", catalog)
catalog.close()
print("Welcome to", l)

# Person Creation
people = [Person("Adam", "Elk"), Person("Barbara", "Field"), Person("Charles", "Grant"), Person("Dylan", "Hilt")]
for p in people:
  print("Welcome,", p)

# Checkout
Divider()
for p in people:
  for n in range(3):
    newBook = random.choice(l.catalog)
    l.checkout(newBook, p, True)
# Technicality
Divider()
l.checkout(l.catalog[0], people[0], True)
l.checkout(l.catalog[0], people[1], True)
l.turn_in(l.catalog[0], people[0], True)
l.turn_in(l.catalog[0], people[1], True)
l.checkout(l.catalog[0], people[1], True)
print(people)

# Book Creation
Divider()
b = Book("Ross Boss Cookbook", "Joshua Ross")
print(f"{b}, formed out of thin air.")
l.checkout(b, people[2], True)
# Technicality
print(f"Adding {b}, to library")
l += b
l += l.catalog[0]
l.checkout(b, people[3], True)
print(f"Removing {b}, from library")
l -= b
l.turn_in(b, people[3], True)
print(f"NOW removing {b}, from library")
l -= b