class Game:

    def __init__(self,game_name,start_time,game_people):
        self.game_name = game_name
        self.start_time = start_time
        self.game_people = game_people

    #遊戲名稱
    def get_game_name(self):
        return self.game_name
    
    #開始時間
    def get_start_time(self):
        return self.start_time
        
    #玩家人數
    def get_game_people(self):
        return self.game_people
    
    
G1=Game('遊戲1','2:00','10')
G2=Game('遊戲2','5:30','12')
G3=Game("遊戲3",'8:00','8')

print("遊戲名稱-1:",G1.get_game_name())
print("開始時間-1:",G1.get_start_time())
print("玩家人數-1:",G1.get_game_people())

print("遊戲名稱-2:",G2.get_game_name())
print("開始時間-2:",G2.get_start_time())
print("玩家人數-2:",G2.get_game_people())

print("遊戲名稱-3:",G3.get_game_name())
print("開始時間-3:",G3.get_start_time())
print("玩家人數-3:",G3.get_game_people())
        