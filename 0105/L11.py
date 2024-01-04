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

"""
副函式EX
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
result = obj1.method1(a, b, c) #呼叫副函式method1,將結果存入變數result中
print(result) 
"""