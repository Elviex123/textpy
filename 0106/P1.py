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

print("1-遊戲名稱:",G1.get_game_name())
print("1-開始時間:",G1.get_start_time())
print("1-玩家人數:",G1.get_game_people())

print("2-遊戲名稱:",G2.get_game_name())
print("2-開始時間:",G2.get_start_time())
print("2-玩家人數:",G2.get_game_people())

print("3-遊戲名稱:",G3.get_game_name())
print("3-開始時間:",G3.get_start_time())
print("3-玩家人數:",G3.get_game_people())
        