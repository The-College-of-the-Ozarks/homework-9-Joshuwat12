# Prog1-HW9

---

In this final homework project, you will be building from scratch three classes, appropriately organized into separate files, as well as writing a program to test their functionality. Unlike many of the previous assignments, this homework will have no user input -- we are testing how well our classes work, not using them to execute specific tasks at this time (remember, OOP desires reusable code). Follow the requirements outlined below for each of the classes and the test suite. Feel free to add any extra desired attributes and methods as you see fit, rename attributes or methods, etc.

We are constructing a library management system. This requires the classes Person, Book, and Library to be defined.

- class Person:
  - Attributes:
    - First Name (str)
    - Last Name (str)
    - Current book list (list of Books - all books currently checked out)
  - Methods:
    - \_\_init\_\_() with parameters for first and last name
    - \_\_repr\_\_() with no extra parameters that shows everything about the class
    - print_name() with no extra parameters that prints only the name
    - print_current_books() with no extra parameters that prints all currently checked out books (name/author only)
    - \_\_len\_\_() with no extra parameters that returns the number of books currently checked out
- class Book:
  - Attributes:
    - Name (str)
    - Author (str)
    - Status (bool - True if available, False if checked out)
    - Previous Borrowers (list of Persons - all people who have previously borrowed *and returned* this book)
    - Current Borrower (Person)
  - Methods:
    - \_\_init\_\_() with parameters for Name and Author
    - \_\_repr\_\_() with no extra parameters that shows everything about the class
    - print_name_author() with no extra parameters that prints name and author only
    - print_status() with no extra parameters that prints the current status (in a meaningful way) including the current borrower if applicable
    - print_prev_borrowers() with no extra parameters that prints the list of previous borrowers (names only)
    - \_\_len\_\_() with no extra parameters that returns the number of previous borrowers
    - \_\_eq\_\_() which returns True if the name and author the same, False otherwise
- class Library:
  - Attributes:
    - Name (str)
    - Catalog (list of Books - all books in the library catalog (both available and checked out)
  - Methods:
    - \_\_init\_\_() with parameters for name and a file storing the catalog (*this method has been provided for you already -- it assumes the file has already been successfully opened for reading*)
    - \_\_repr\_\_() with no extra parameters that shows everything about the class
    - print_catalog() with no extra parameters that prints the entire catalog with status
    - print_available() with no extra parameters that prints all available books
    - print_unavailable() with no extra parameters that prints all unavailable books and who has them
    - checkout() with parameters for a Book and a Person. If the book is in the catalog and available, mark it as unavailable, update it's current borrower, and update the current book list of the borrower. Otherwise, output an appropriate error message
    - turn_in() with parameters for a Book and a Person. If the person has that book checked out, mark it as available in the catalog, move it's current borrower to the previous borrowers list, and update the current book list of the borrower. Otherwise, output an appropriate error message
    - \_\_add\_\_() which adds a Book to the catalog if it is not already, otherwise output an appropriate error message
    - \_\_sub\_\_() which removes a Book from the catalog if it is in the catalog and available, otherwise output an appropriate error message
    - \_\_len\_\_() with no extra parameters that returns the size of the catalog


Your main program should thoroughly test and exhibit the successful operation of all aspects of your code with no user input required (that is, I should be able to run your code then just look over the output to see that things worked correctly, never being required to type anything). You may wish to include more than this, but at bare minimum your main program should do the following, in any order:
- Create a Library using the provided catalog file
- Create at least 4 Person objects
- Have each Person check out/in at least three books with the Library
- At least once, have a person check out a book that somebody else has already returned
- At least once, have a person attempt to check out an unavailable book
- At least once, have a person attempt to check out a book not in the catalog
- At least once, have a person attempt to return a book they don't have
- At least once, add a book to the catalog
- At least once, remove a book from the catalog
- At least once, attempt to add a book that is already in the catalog
- At least once, attempt to remove a book that is unavailable


***Bonus:*** Modify the Library \_\_init\_\_() function to allow for an optional "status" of each book (default to available) and add the ability to output the current catalog to a file. Exhibit the functionality by creating a new Library with the output catalog.
