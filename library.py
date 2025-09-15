from collections import deque

# Node for Linked List
class BookNode:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity
        self.next = None

class Library:
    def __init__(self):
        self.head = None
        self.issue_queue = deque()     # stores (book_id, user)

    # Add new book
    def add_book(self, book_id, title, author, quantity):
        new_book = BookNode(book_id, title, author, quantity)
        if not self.head:
            self.head = new_book
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_book
        print("✅ Book added successfully!")

    # Display all books
    def display_books(self):
        if not self.head:
            print("📭 No books in the library.")
            return
        temp = self.head
        print("\n--- Library Books ---")
        while temp:
            print(f"ID: {temp.book_id} | Title: {temp.title} | "
                  f"Author: {temp.author} | Quantity: {temp.quantity}")
            temp = temp.next

    # Search book by ID
    def search_book(self, book_id):
        temp = self.head
        while temp:
            if temp.book_id == book_id:
                print(f"🔍 Found -> {temp.title} by {temp.author}, "
                      f"Qty: {temp.quantity}")
                return temp
            temp = temp.next
        print("❌ Book not found.")
        return None

    # Delete book
    def delete_book(self, book_id):
        temp = self.head
        prev = None
        while temp:
            if temp.book_id == book_id:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print("🗑 Book deleted.")
                return
            prev = temp
            temp = temp.next
        print("❌ Book not found.")

    # Issue book
    def issue_book(self, book_id, user):
        book = self.search_book(book_id)
        if book and book.quantity > 0:
            book.quantity -= 1
            self.issue_queue.append((book_id, user))
            print(f"📖 '{book.title}' issued to {user}.")
        else:
            print("⚠ Book not available.")

    # Return book
    def return_book(self, book_id, user):
        if (book_id, user) in self.issue_queue:
            self.issue_queue.remove((book_id, user))
            book = self.search_book(book_id)
            if book:
                book.quantity += 1
                print(f"✅ {user} returned '{book.title}'.")
        else:
            print("❌ No record of this issue.")

# ----------- MAIN PROGRAM -----------
def main():
    lib = Library()
    while True:
        print("\n====== Library Menu ======")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            bid = int(input("Enter Book ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            qty = int(input("Enter Quantity: "))
            lib.add_book(bid, title, author, qty)

        elif choice == "2":
            lib.display_books()

        elif choice == "3":
            bid = int(input("Enter Book ID to search: "))
            lib.search_book(bid)

        elif choice == "4":
            bid = int(input("Enter Book ID to delete: "))
            lib.delete_book(bid)

        elif choice == "5":
            bid = int(input("Enter Book ID to issue: "))
            user = input("Enter User Name: ")
            lib.issue_book(bid, user)

        elif choice == "6":
            bid = int(input("Enter Book ID to return: "))
            user = input("Enter User Name: ")
            lib.return_book(bid, user)

        elif choice == "7":
            print("👋 Exiting Library System.")
            break
        else:
            print("⚠ Invalid choice!")

if __name__ == "__main__":
    main()