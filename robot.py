import env

#下棋的机器人类
class Crobot():
    def __init__(self):
        self.flag=1  #机器人执蓝为1，执红色为-1
    def move(self,m):
        if m[1][1]!=self.flag:
            return 1,1
        else:
            return 2,0


