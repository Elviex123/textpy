class Library:
    def __init__ (self,book,id):
        self.book = book
        self.id = id

    def get_book(self):
        return self.book
    
    def get_id(self):
        return self.id
l1=Library('BOOK','IDD')
print("書名",l1.get_book())
print("書ID",l1.get_id())