class Library:
    def __init__(self,book_name,book_id,book_author,book_publisher,bookpublisher_date,borrow_if,borrow_date,borrow_ddl,book_location,student_name,student_id,student_email):
        self.book_name = book_name
        self.book_id = book_id
        self.book_author = book_author
        self.book_publisher = book_publisher
        self.bookpublisher_date = bookpublisher_date
        self.borrow_if = borrow_if
        self.borrow_date = borrow_date
        self.borrow_ddl = borrow_ddl
        self.book_location = book_location
        self.student_name = student_name
        self.student_id = student_id
        self.student_email = student_email

    #列印資訊
    def print_library_info(self):
        print("書名:",self.book_name)
        print("書ID:",self.book_id)
        print("作者:",self.book_author)
        print("出版社:",self.book_publisher)
        print("還書期限:",self.bookpublisher_date)
        print("是否借出:",self.borrow_if)
        print("借出日期:",self.borrow_date)
        print("還書期限:",self.borrow_ddl)
        print("館藏位置:",self.book_location)
        print("借書人名字:",self.student_name)
        print("借書人ID:",self.student_id)
        print("借書人EMAIL:",self.student_email)
#建立物件
b1= Library('PYTHON','111','Author','Publisher','2022-01-01','Yes','2023-01-01','2023-02-01','A103','Sname','Sid','Semail')
#印出課程資訊
b1.print_library_info()

