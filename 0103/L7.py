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
        
    def get_book_name(self):
        return self.book_name
    
    def get_book_id(self):
        return self.book_id
    
    def get_book_author(self):
        return self.book_author
    
    def get_book_publisher(self):
        return self.book_publisher
    
    def get_publisher_date(self):
        return self.bookpublisher_date
    
    def is_borrowed(self):
        return self.borrow_if
    
    def get_borrow_date(self):
        return self.borrow_date
    
    def get_borrow_deadline(self):
        return self.borrow_ddl
    
    def get_location(self):
        return self.book_location
    
# 建立物件
b1= Library('PYTHON','111','Author','Publisher','2022-01-01','Yes','2023-01-01','2023-02-01','A103','Sname','Sid','Semail')

# 使用新的副函式取得資訊
print("書名:", b1.get_book_name())
print("書ID:", b1.get_book_id())
print("作者:", b1.get_book_author())
print("出版社:", b1.get_book_publisher())
print("出版日期:", b1.get_publisher_date())
print("是否借出:", b1.is_borrowed())
print("借出日期:", b1.get_borrow_date())
print("還書期限:", b1.get_borrow_deadline())
print("館藏位置:", b1.get_location())


"""副函式EX
class A(object):
    #副函式定義，名稱為method1，參數有a,b,c
    def method1(self, a, b, c):
        # 副函式程式內容，計算3個數字相乘的積
        return a*b*c
           
 
#呼叫副函式，先建立類別物件
obj1 = A()
#再利用建立好的類別物件obj1呼叫副函式method1
a=1
b=2
c=3
result = obj1.method1(a, b, c) #呼叫副函式method1，將結果存入變數result中
print(result) #列印結果

"""