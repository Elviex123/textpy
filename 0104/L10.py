class Library:
    def __init__ (self,book_name,book_id,book_author,book_publisher,book_location):
        self.book_name = book_name
        self.book_id = book_id
        self.book_author = book_author
        self.book_publisher =book_publisher
        self.book_location = book_location

    def get_book_name(self):
        return self.book_name
    
    def get_book_id(self):
        return self.book_id
    
    def get_book_author(self):
        return self.book_author
    
    def get_book_publisher(self):
        return self.book_publisher
    
    def get_book_location(self):
        return self.book_location
    
l1=Library('書本','12345','作者','出版社','位置')
print("書名",l1.get_book_name())
print("書ID",l1.get_book_id())
print("作者",l1.get_book_author())
print("出版社",l1.get_book_publisher())
print("位置",l1.get_book_location())
    