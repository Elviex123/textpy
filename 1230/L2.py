"""
1.class pass
2.建構子定義 def __init__(self,...)
3.屬性(書名 書ID 作者 出版社 出版日期 是否借出 借出日期 還書期限 館藏位置 借書人姓名 學號 EMAIL)
4.副函式:可查詢書名 ID 作者 出版社 是否借出 借出日期 借書人所借書單 
5.建立物件 呼叫副函式
"""
class Library:
    def __init__(self, book_name, book_id, author, publisher, publication_date, borrowed=False, borrowed_date=None, return_deadline=None, location=None, borrower_name=None, student_id=None, email=None):
        self.book_name = book_name
        self.book_id = book_id
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
        self.borrowed = borrowed
        self.borrowed_date = borrowed_date
        self.return_deadline = return_deadline
        self.location = location
        self.borrower_name = borrower_name
        self.student_id = student_id
        self.email = email

    def check_book_details(self):
        # 檢視書籍詳細資訊
        details = f"書名: {self.book_name}\n書ID: {self.book_id}\n作者: {self.author}\n出版社: {self.publisher}\n是否借出: {self.borrowed}\n"
        if self.borrowed:
            details += f"借出日期: {self.borrowed_date}\n借書人姓名: {self.borrower_name}\n借書人學號: {self.student_id}\nEmail: {self.email}\nReturn Deadline: {self.return_deadline}\n"
        return details

    def borrow_book(self, borrower_name, student_id, email, borrowed_date, return_deadline):
        # 借出書籍
        if not self.borrowed:
            self.borrowed = True
            self.borrower_name = borrower_name
            self.student_id = student_id
            self.email = email
            self.borrowed_date = borrowed_date
            self.return_deadline = return_deadline
            return f"{self.book_name} has been borrowed by {borrower_name}."
        else:
            return f"{self.book_name} is already borrowed."

    def return_book(self):
        # 歸還書籍
        if self.borrowed:
            self.borrowed = False
            self.borrower_name = None
            self.student_id = None
            self.email = None
            self.borrowed_date = None
            self.return_deadline = None
            return f"{self.book_name} has been returned."
        else:
            return f"{self.book_name} is not currently borrowed."

    def update_publication_date(self, new_publication_date):
        # 更新書籍的出版日期
        self.publication_date = new_publication_date
        #return f"{self.book_name}'s publication date has been updated to {new_publication_date}."



# 示例操作
book1 = Library("Python Programming", "ISBN123", "John Doe", "Publisher A", "2023-01-01", False)
print(book1.check_book_details())

new_date = "2024-01-15"
print(book1.update_publication_date(new_date))


print(book1.borrow_book("Alice", "S12345", "alice@example.com", "2023-12-30", "2024-01-30"))
print(book1.check_book_details())

print(book1.return_book())
print(book1.check_book_details())
