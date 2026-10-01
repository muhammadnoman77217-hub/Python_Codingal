class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have successfully borrowed '{self.title}' by {self.author}")
        else:
            print(f"Sorry, '{self.title}' is currently already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You have successfully returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")

book1 = Book("1984", "George Orwell")
book2 = Book("To kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "f. Scott Fitzgerald")

print("--- Borrowing Books ---")
book1.borrow()
book2.borrow()

print("\n---Returning Books ---")
book1.return_book()
book3.return_book()