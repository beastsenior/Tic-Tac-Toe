import random
import brain
import numpy as np

#下棋的机器人类
class Crobot():
    def __init__(self,flag,mode):  #flag指定机器人执蓝为1，执红色为-1；mode指定运行模式：0为随机模式brain_random，
        self.flag=flag
        self.mode=mode
        if mode==1:
            self.brain_dqn_train=brain.Cbrain()
        if mode==2:
            self.brain_dqn_train_sv=brain.Cbrain()

    def move(self,s,movemode=-1):  #movemode用于指定这一步的模式：默认-1为跟随生成机器人时的指定，0为随机下法，1为DQN训练模式，2为DQN专家模式
        if movemode==-1:
            movemode=self.mode

        #随机模式
        if movemode==0:
            x,y= self.brain_random(s)
            return x,y,self.flag

        #DQN训练模式，输出动作值
        if movemode==1:
            #选动作
            a=self.brain_dqn_train.choose_action(s)
            x,y =divmod(a,3)  #divmod(x,y)这个函数可以获得商和余数，比如divmod(5,2)，返回的值为(2,1)，其中2为商，1为余数
            return x,y,self.flag

        #DQN训练模式，输出盘面值
        if movemode==2:
            # #先随机选个动作
            # while 1:
            #     x = random.randrange(0, 3)
            #     y = random.randrange(0, 3)
            #     if s[x * 3 + y] == 0.:
            #         i_max=x*3+y
            #         break

            v=[0.]*9
            i_flag = 0  # 判断是否是第一次赋值给v_max和i_max
            #遍历动作，找盘面估值最大的
            for i in range(9):
                if s[i]==0.:
                    s_tmp=s.copy()
                    s_tmp[i]=self.flag*0.5
                    v[i]=self.brain_dqn_train_sv.get_value(s_tmp)
                    if i_flag==0:
                        v_max=v[i]
                        i_max=i
                        i_flag=1
                    elif v[i]>v_max:
                        v_max=v[i]
                        i_max=i
            x,y=divmod(i_max,3)
            return x,y,self.flag


        #DQN专家模式（提取已经训练好的神经网络）
        #if movemode==3:

    def brain_random(self, s):  # 随机模式
        while 1:
            x = random.randrange(0, 3)
            y = random.randrange(0, 3)
            if s[x*3+y] == 0.:
                return x, y

    def m2s(self,m):
        # 把棋盘局面m转化为神经网络识别的float形式
        s = np.zeros(9, dtype=np.float32)
        k = 0
        for i in range(3):
            for j in range(3):
                s[k] = np.float32(m[i][j]/2)
                k += 1
        return s





