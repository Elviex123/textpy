"""
1.class pass
2.建構子定義 def __init__(self,...)
3.屬性(書名 書ID 作者 出版社 出版日期 是否借出 借出日期 還書期限 館藏位置 借書人姓名 學號 EMAIL)
4.副函式:可查詢書名 ID 作者 出版社 是否借出 借出日期 借書人所借書單 
5.建立物件 呼叫副函式
"""
#分批列印 有多個副函式
class Library:
    def __init__(self,book_name,book_id,book_author,book_publisher,publisher_date,borrow_if,borrow_date,book_date,location,student_name,student_id,student_email):
        self.__book_name = book_name 
        self.__book_id = book_id
        self.__book_author = book_author
        self.__book_publisher = book_publisher
        self.__publisher_date = publisher_date
        self.__borrow_if = borrow_if
        self.__borrow_date = borrow_date
        self.__book_date = book_date
        self.__location = location
        self.__student_name = student_name
        self.__student_id = student_id
        self.__student_email = student_email
    #書名
    def get_book_name(self):
        return self.__book_name
    #書ID
    def get_book_id(self):
        return self.__book_id
    #作者
    def get_book_author(self):
        return self.__book_author
    
    def get_book_publisher(self):
        return self.__book_publisher
    
    def get_publisher_date(self):
        return self.__publisher_date
    
    def get_borrow_if(self):
        return self.__borrow_if
    
    def get_borrow_date(self):
        return self.__borrow_date
    
    def get_book_date(self):
        return self.__book_date
    
    def get_location(self):
        return self.__location
    
    def get_student_name(self):
        return self.__student_name
    
    def get_student_id(self):
        return self.__student_id
    
    def get_student_email(self):
        return self.__student_email

#建立資料
b1= Library('Java',
            '111',
            'java_author',
            'publisher_name',
            '2022-01-01',
            'Yes',
            '2023-01-01',
            '2023-02-01',
            'Library_location',
            'Student_name',
            'Student_id',
            'student_email@example.com')
print("書名=", b1.get_book_name())
print("書id=", b1.get_book_id())
print("書的作者=", b1.get_book_author())
print("書的出版社=", b1.get_book_publisher())
print("出版日期=", b1.get_publisher_date())
print("是否借出=", b1.get_borrow_if())
print("借出日期=", b1.get_borrow_date())
print("還書期限=", b1.get_book_date())
print("館藏位置=", b1.get_location())
print("借書人姓名=", b1.get_student_name())
print("借書人學號=", b1.get_student_id())
print("借書人EMAIL=", b1.get_student_email())