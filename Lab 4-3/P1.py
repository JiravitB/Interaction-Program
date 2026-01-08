"""
Jiravit Boonyaritchaikit
683040154-3
P1
"""

from Library import LibraryItem, Book, TextBook, Magazine



Library = LibraryItem("Pen","P001")
Library.get_status()
Library.display()
Library.check_out()
Library.display()
Library.return_item()
Library.display()
print("========================================\n")

book = Book("Harry Potter", "B001", "J.K. Rowling")
book.get_status()
book.set_pages(300)
book.display_info()
book.check_out()
book.display_info()
book.return_item()
book.display_info()
print("========================================\n")

text = TextBook("Time","T001","GU","History","High school")
text.get_status()
text.set_pages(250)
text.display_info()
text.check_out()
text.display_info()
text.return_item()
text.display_info()
print("========================================\n")

mag = Magazine("TIME","M001",200)
mag.get_status()
mag.display()
mag.check_out()
mag.display()
mag.return_item()
mag.display()
print("========================================\n")