class Library:
    def __init__(self,book_name,book_id,book_author,book_publisher,book_location,student_name,student_id,student_email,borrow_if,borrow_date,borrow_ddl):
        self.book_name = book_name
        self.book_id = book_id
        self.book_author = book_author
        self.book_publisher = book_publisher
        self.book_location = book_location

        self.student_name = student_name
        self.student_id = student_id
        self.student_email = student_email

        self.borrow_if = borrow_if
        self.borrow_date = borrow_date
        self.borrow_ddl = borrow_ddl

    def get_book_name(self):
        return self.book_name #miss

    def get_book_id(self):
        return self.book_id
    
    def get_book_author(self):
        return self.book_author
    
    def get_book_publisher(self):
        return self.book_publisher
    
    def get_book_location(self):
        return self.book_location

    def get_student_name(self):
        return self.student_name
    
    def get_student_id(self):
        return self.student_id
    
    def get_student_email(self):
        return self.student_email
    
    def get_borrow_if(self):
        return self.borrow_if

    def get_borrow_date(self):
        return self.borrow_date
    
    def get_borrow_ddl(self):
        return self.borrow_ddl
    
l1=Library('PYTHON','100','author','publisher','a101','myname1','myid1','myenail1','yes','2024/01/01','2024/01/11')
l2=Library('C++','200','author2','publisher2','a102','myname2','myid2','myenail2','no','2024/01/02','2024/01/12')
print("書名1",l1.get_book_name())
print("書id1",l1.get_book_id())
print("作者1",l1.get_book_author())
print("出版社1",l1.get_book_publisher())
print("位置1",l1.get_book_location())
print("學生名1",l1.get_student_name())
print("學生id1",l1.get_student_id())
print("學生email1",l1.get_student_email())
print("是否借閱1",l1.get_borrow_if())
print("借閱日期1",l1.get_borrow_date())
print("截止日期1",l1.get_borrow_ddl())

print("書名2",l2.get_book_name())
print("書id2",l2.get_book_id())
print("作者2",l2.get_book_author())
print("出版社2",l2.get_book_publisher())
print("位置2",l2.get_book_location())
print("學生名2",l2.get_student_name())
print("學生id2",l2.get_student_id())
print("學生email2",l2.get_student_email())
print("是否借閱2",l2.get_borrow_if())
print("借閱日期2",l2.get_borrow_date())
print("截止日期2",l2.get_borrow_ddl())
