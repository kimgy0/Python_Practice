names=["Messi","Romas","Ronaldo","Par","Buffon"]
positions=["MF","DF","CF","WF","GK"]
numbers=[10,4,7,13,1]

players=[[name,position,number]for name, position,number in zip(names,positions,numbers)]
print(players)
print(players[0])

#soccerplayer code
class SoccerPlayer(object):
    def __init__(self,name,position,back_number):
        self.name=name
        self.position=position
        self.back_number=back_number
    def change_back_number(self,new_number):
        print("선수의 등번호를 변경한다 : From {0} to {1}".format(self.back_number,new_number))
        self.back_number=new_number
    def __str__(self):
        return "Hello, My name is {0} I play in {1} in center".format(self.name,self.position)

#class instance
player_objects=[SoccerPlayer(name,position,number) for name,position,number in zip(names,positions,numbers)]
print(player_objects[0])
print(player_objects[1])
print(player_objects[2])
print(player_objects[3])
print(player_objects[4])