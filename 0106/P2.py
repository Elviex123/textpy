
"""
輸入行李ID ,輸出所有資訊
主函示3個物件 使用查詢行李和修改資訊對每一個屬性寫修改資訊的副函示共五個 查詢行李
"""
#行李類別
class Luggage:
    def __init__(self,lg_id,lg_weight,lg_start_airport,lg_last_airport,lg_name):
        self._lg_id = lg_id
        self._lg_weight = lg_weight
        self._lg_start_airport = lg_start_airport
        self._lg_last_airport = lg_last_airport
        self._lg_name = lg_name

    #行李ID
    def get_lg_id(self):
        return self._lg_id 
    
    #行李重量
    def get_lg_weight(self):
        return self._lg_weight
    
    #行李出發機場
    def get_lg_start_airport(self):
        return self._lg_start_airport
    
    #行李目的地機場
    def get_lg_last_airport(self):
        return self._lg_last_airport
    
    #行李所屬旅客姓名
    def get_lg_name(self):
        return self._lg_name
#登機證類別
class Boardingpass:
    def __init__(self,passenger_name,boardingpass_number,boarding_time,boardinggate_number,passenger_location,luggage_number,luggage_id):
        self._passenger_name = passenger_name
        self._boardingpass_number = boardingpass_number
        self._boarding_time = boarding_time
        self._boardinggate_number = boardinggate_number
        self._passenger_location = passenger_location
        self._luggage_number = luggage_number
        self._luggage_id = luggage_id

    #旅客姓名
    def get_passenger_name(self):
        return self._passenger_name
    
    #登機證編號
    def get_boardingpass_number(self):
        return self._boardingpass_number
    
    #登機時間
    def get_boarding_time(self):
        return self._boarding_time
    
    #登機門編號
    def get_boardinggate_number(self):
        return self._boardinggate_number
    
    #座位位置
    def get_passenger_location(self):
        return self._passenger_location
    
    #行李件數 
    def get_luggage_number(self):
        return self._luggage_number
    
    #行李ID
    def get_luggage_id(self):
        return self._luggage_id
    
#主函式
def main():  
    #定義行李資訊
    L1=Luggage('001','10','松山機場','仁川機場','Amy')
    L2=Luggage('002','11','仁川機場','松山機場','John')
    L3=Luggage('003','12','桃園國際機場','仁川機場','Tina')

    print("行李ID1:",L1.get_lg_id())
    print("行李重量1:",L1.get_lg_weight())
    print("行李出發機場1:",L1.get_lg_start_airport())
    print("行李目的地機場1:",L1.get_lg_last_airport())
    print("行李所屬旅客姓名1:",L1.get_lg_name())
    print("  ")
    print("行李ID1:",L2.get_lg_id())
    print("行李重量2:",L2.get_lg_weight())
    print("行李出發機場2:",L2.get_lg_start_airport())
    print("行李目的地機場2:",L2.get_lg_last_airport())
    print("行李所屬旅客姓名2:",L2.get_lg_name())
    print("  ")
    print("行李ID3:",L3.get_lg_id())
    print("行李重量3:",L3.get_lg_weight())
    print("行李出發機場3:",L3.get_lg_start_airport())
    print("行李目的地機場3:",L3.get_lg_last_airport())
    print("行李所屬旅客姓名3:",L3.get_lg_name())

    #列印登機證資訊
    #登機證物件1
    B1 = Boardingpass('Ann','100','8:00','1','A101','1','001')
    #登機證物件2
    B2 = Boardingpass('Bob','200','10:00','2','B202','2','002')
    #登機證物件3
    B3 = Boardingpass('Cindy','300','12:00','1','C303','1','003')
    print(" ")
    #列印登機證資訊1
    print("旅客姓名1:",B1.get_passenger_name())
    print("登機證編號1:",B1.get_boardingpass_number())
    print("登機時間1:",B1.get_boarding_time())
    print("登機門編號1:",B1.get_boardinggate_number())
    print("座位位置1:",B1.get_passenger_location())
    print("行李件數1:",B1.get_luggage_number())
    print("行李ID1:",B1.get_luggage_id())
    print("  ")
    #列印登機證資訊2
    print("旅客姓名2:",B2.get_passenger_name())
    print("登機證編號2:",B2.get_boardingpass_number())
    print("登機時間2:",B2.get_boarding_time())
    print("登機門編號2:",B2.get_boardinggate_number())
    print("座位位置2:",B2.get_passenger_location())
    print("行李件數2:",B2.get_luggage_number())
    print("行李ID2:",B2.get_luggage_id())
    print("  ")
    #列印登機證資訊3
    print("旅客姓名3:",B3.get_passenger_name())
    print("登機證編號3:",B3.get_boardingpass_number())
    print("登機時間3:",B3.get_boarding_time())
    print("登機門編號3:",B3.get_boardinggate_number())
    print("座位位置3:",B3.get_passenger_location())
    print("行李件數3:",B3.get_luggage_number())
    print("行李ID3:",B3.get_luggage_id())

if __name__=="__main__":
    main()

"""
-列印資訊
- 修改的副函示
    -個列印富含是&
    修改副函式
    -主函示MAIN中建立2-3個登機證物件 
    -分別呼叫14(7*2)個副函式屬姓
    """