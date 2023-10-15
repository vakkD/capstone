
#library class
class LibraryItem:
    def __init__(self, item_name, author, publisher):
        self.item_name =item_name
        self.author =author
        self.publisher =publisher

    def get_details(self):
        return self.item_name, self.author, self.publisher
    
    
#tester
item1 =LibraryItem('Book1', 'Author1', 'Publisher1')
item2 =LibraryItem('Book2', 'Author2', 'Publisher2')
item3 =LibraryItem('Book3', 'Author3', 'Publisher3')

print(item1.get_details())
print(item2.get_details())
print(item3.get_details())

#book class
class Book(LibraryItem):
    def __init__(self, item_name, author, publisher, num_pages, is_ebook =False, is_hardcopy =False):
        super().__init__(item_name, author, publisher)
        self.num_pages =num_pages
        self.is_ebook =is_ebook
        self.is_hardcopy =is_hardcopy

    def get_details(self):
        return super().get_details(), self.num_pages, self.is_ebook, self.is_hardcopy
    
#main
book =Book('Book', 'Author', 'Publisher', 200, True, True)
print(book.get_details())