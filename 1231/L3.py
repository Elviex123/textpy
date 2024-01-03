"""
1.class pass
2.建構子定義 def __init__(self,...)
3.屬性(書名 書ID 作者 出版社 出版日期 是否借出 借出日期 還書期限 館藏位置 借書人姓名 學號 EMAIL)
4.副函式:可查詢書名 ID 作者 出版社 是否借出 借出日期 借書人所借書單 
5.建立物件 呼叫副函式
"""
#印出全部 副函式整合

class Library:
    def __init__(self,book_name,book_id,book_author,book_publisher,publisher_date,borrow_if,borrow_date,borrow_book_date,location,student_name,student_id,student_email):
        self.book_name = book_name
        self.book_id = book_id
        self.book_author = book_author
        self.book_publisher = book_publisher
        self.publisher_date = publisher_date
        self.borrow_if = borrow_if
        self.borrow_date = borrow_date
        self.borrow_book_date = borrow_book_date
        self.location = location
        self.student_name = student_name
        self.student_id = student_id
        self.student_email = student_email

    def get_book_info(self):
        return f"書名:{self.book_name}\n書ID:{self.book_id}\n作者:{self.book_author}\n出版社:{self.book_publisher}\n出版日期:{self.publisher_date}\n館藏位置:{self.location}\n借書人姓名:{self.student_name}\n借書人學號:{self.student_id}\n借書人EMAIL:{self.student_email}"

    def get_borrow(self):
        return f"是否借出:{self.borrow_if}\n借出日期:{self.borrow_date}\n還書期限:{self.borrow_book_date}"

book = Library(
    book_name="Python",
    book_id="12345",
    book_author="Author",
    book_publisher="222",
    publisher_date="2022/12/31",
    location="A301",
    student_name="MYNAME",
    student_id="4b1k0026",
    student_email="4b1k0026@stust.edu.tw",  

    borrow_if="是",
    borrow_date="2024/01/01",
    borrow_book_date="2024/01/11"
) 

if __name__ == "__main__":
    print("Correct!\n")
    print(book.get_book_info())
    print(book.get_borrow())






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