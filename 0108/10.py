class Product :
    def __init__(self,product_name,product_date,purchaser):
            self.product_name= product_name
            self.product_date= product_date
            self.purchaser= purchaser

#商品名稱
    def get_product_name(self):
        return self.product_name

#商品製造日期
    def get_product_date(self) : 
        return self.product_date

#商品購買人名字
    def get_purchaser(self):
        return self.purchaser

#定義商品物件
a1= Product ('玩偶','2023-09-23','bl')
b1= Product ('玩偶','2023-12-04','tjr')
c1= Product ('玩偶','2023-12-20','dylan')

print("商品名稱1",a1.get_product_name())
print("商品製造日期1",a1.get_product_date())
print("商品購買人名字1",a1.get_purchaser())

print("商品名稱2",b1.get_product_name())
print("商品製造日期2",b1.get_product_date())
print("商品購買人名字2",b1.get_purchaser())  

print("商品名稱3",c1.get_product_name())
print("商品製造日期3",c1.get_product_date())
print("商品購買人名字3",c1.get_purchaser())

"""
a1= Product ('玩偶','2023-09-23','bl')
b1= Product ('玩偶','2023-12-04','tjr')
c1= Product ('玩偶','2023-12-20','dylan')

print("商品名稱1",a1.get_product_name())
print("商品製造日期1",a1.get_product_date())
print("商品購買人名字1",a1.get_purchaser())

print("商品名稱2",b1.get_product_name())
print("商品製造日期2",b1.get_product_date())
print("商品購買人名字2",b1.get_purchaser())  

print("商品名稱3",c1.get_product_name())
print("商品製造日期3",c1.get_product_date())
print("商品購買人名字3",c1.get_purchaser())

"""