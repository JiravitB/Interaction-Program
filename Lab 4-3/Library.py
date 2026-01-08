"""
Jiravit Boonyaritchaikit
683040154-3
Library
"""
from datetime import datetime
class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self._id = item_id
        self._checked_out = False
    
    def get_status(self):
        return "Checked out" if self._checked_out else "Available"
    
    def check_out(self):
        # if checked_out is False (item still in lib)
        if not self._checked_out:
            self._checked_out = True
            return True
        # can't check out if item not in lib
        return False

    def return_item(self):
        if self._checked_out:
            self._checked_out = False
            return True
        return False
    
    def display(self):
        print(f"Title: {self.title}")
        print(f"ID: {self._id}")
        print(f"Status: {self.get_status()}")


# implement 3 classes here
class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author
        self.pages_count = 0
    
    def set_pages(self,pages):
        self.pages_count = pages
        return pages
    
    def display_info(self):

        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages_count}")
        print(f"Status: {self.get_status()}")

class TextBook(Book):
    def __init__(self, title, item_id, author, subject, grade):
        super().__init__(title, item_id, author)
        self.subject = subject
        self.grade_level = grade

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")
        print(f"grade: {self.grade_level}\n")

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_num):
        super().__init__(title, item_id)
        self.issue = issue_num
        
        now = datetime.now()
        self.month = now.month
        self.year = now.year

    def display(self):
        super().display()
        print(f"issue number: {self.issue}")
        print(f"month: {self.month}")
        print(f"year: {self.year}\n")
# Test your code:
# This is just an example. You should test a lot more than this.