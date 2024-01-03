

class Library:
    def __init__(self, book_title, book_id, author, publisher, publish_date, is_borrowed=False, borrow_date=None,
                 return_deadline=None, location=None, borrower_name=None, student_id=None, email=None):
        # 初始化圖書相關資訊
        self.book_title = book_title
        self.book_id = book_id
        self.author = author
        self.publisher = publisher
        self.publish_date = publish_date
        self.is_borrowed = is_borrowed
        self.borrow_date = borrow_date
        self.return_deadline = return_deadline
        self.location = location
        self.borrower_name = borrower_name
        self.student_id = student_id
        self.email = email

    def get_book_info(self):
        # 取得圖書詳細資訊
        return f"書名: {self.book_title}\n書ID: {self.book_id}\n作者: {self.author}\n出版社: {self.publisher}\n是否借出: {self.is_borrowed}\n借出日期: {self.borrow_date}\n借書人姓名: {self.borrower_name}\n學號: {self.student_id}\nEMAIL: {self.email}"

    def check_borrow_status(self):
        # 檢查借閱狀態
        return f"書名: {self.book_title}\n是否借出: {self.is_borrowed}\n借出日期: {self.borrow_date}\n借書人所借書單: {self.borrower_name}'s Borrowed Books"

# 建立 Library 物件
book = Library(
    book_title="Python Programming",
    book_id="PY101",
    author="John Doe",
    publisher="ABC Publications",
    publish_date="2023-01-01",
    is_borrowed=True,
    borrow_date="2023-12-20",
    borrower_name="Alice",
    student_id="S12345",
    email="alice@example.com"
)

# 呼叫方法取得書籍資訊
print(book.get_book_info())

# 呼叫方法查詢借閱狀態
#print(book.check_borrow_status())
