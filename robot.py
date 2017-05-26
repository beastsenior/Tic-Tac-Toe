import random
import brain

#下棋的机器人类
class Crobot():
    def __init__(self,flag,mode):  #flag指定机器人执蓝为1，执红色为-1；mode指定运行模式：0为随机模式brain_random，
        self.flag=flag
        self.mode=mode
        if mode==1:
            self.brain_dqn_train=brain.Cbrain()

    def move(self,s,movemode=-1):  #movemode用于指定这一步的模式：默认-1为跟随生成机器人时的指定，0为随机下法，1为DQN训练模式，2为DQN专家模式
        if movemode==-1:
            movemode=self.mode

        #随机模式
        if movemode==0:
            x,y= self.brain_random(s)
            return x,y,self.flag

        #DQN训练模式
        if movemode==1:
            #选动作
            a=self.brain_dqn_train.choose_action(s)
            x,y =divmod(a,3)  #divmod(x,y)这个函数可以获得商和余数，比如divmod(5,2)，返回的值为(2,1)，其中2为商，1为余数
            return x,y,self.flag

        #DQN专家模式（提取已经训练好的神经网络）
        #if movemode==2:

    def brain_random(self, s):  # 随机模式
        while 1:
            x = random.randrange(0, 3)
            y = random.randrange(0, 3)
            if s[x*3+y] == 0.:
                return x, y







