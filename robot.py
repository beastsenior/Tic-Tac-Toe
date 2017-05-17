import random

#下棋的机器人类
class Crobot():
    def __init__(self,flag,mode):  #flag指定机器人执蓝为1，执红色为-1；mode指定运行模式：0为随机模式，
        self.flag=flag
        self.mode=mode
    def move(self,m,movemode=-1):  #movemode用于指定这一步的模式：默认-1为跟随生成机器人时的指定，0为随机下法，
        if movemode==-1:
            movemode=self.mode

        #随机模式
        if movemode==0:
            while 1:
                x=random.randrange(0, 3)
                y=random.randrange(0, 3)
                if m[x][y] == 0:
                    return x,y,self.flag



