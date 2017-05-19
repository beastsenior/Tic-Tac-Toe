import tkinter as tk

#显示类，把棋盘数据显示在屏幕
class Cshow(tk.Tk):
    def __init__(self):
        super(Cshow, self).__init__()
        self.title('Tom和Jerry大战井字棋（机器学习）')
        self.geometry('{0}x{1}'.format(600, 600))
        self.canvas = tk.Canvas(self, bg='white', height=600, width=600)         #生成画布
        self.redraw([[0,0,0],[0,0,0],[0,0,0]])

    def redraw(self,m):
        self.canvas.delete("all")  # 清空画布
        #设定棋盘
        BLANK_H = 150  # 棋盘上端空白
        BLANK_W = 150  # 棋盘左端空白
        B_H = 3  # 棋盘高
        B_W = 3  # 棋盘宽
        UNIT = 90  # 棋盘每格大小
        P_S = 60  # 棋子大小
        for c in range(BLANK_W, BLANK_W+(B_W+1)* UNIT, UNIT):
            x0, y0, x1, y1 = c, BLANK_H, c, BLANK_H+B_H* UNIT
            self.canvas.create_line(x0, y0, x1, y1,width=2)
        for r in range(BLANK_H, BLANK_H+(B_H+1)* UNIT, UNIT):
            x0, y0, x1, y1 = BLANK_W, r, BLANK_W+B_W* UNIT, r
            self.canvas.create_line(x0, y0, x1, y1,width=2)
        #设定棋子
        for c in range(0,B_H):
            for r in range(0,B_W):
                if m[c][r]==1:
                    self.oval = self.canvas.create_oval(BLANK_H + r * UNIT + (UNIT - P_S) // 2,
                                                        BLANK_W + c * UNIT + (UNIT - P_S) // 2,
                                                        BLANK_H + (r+1) * UNIT - (UNIT - P_S) // 2,
                                                        BLANK_W + (c+1) * UNIT - (UNIT - P_S) // 2,
                                                        outline='', fill='blue')
                if m[c][r]==-1:
                    self.oval = self.canvas.create_oval(BLANK_H + r * UNIT + (UNIT - P_S) // 2,
                                                        BLANK_W + c * UNIT + (UNIT - P_S) // 2,
                                                        BLANK_H + (r+1) * UNIT - (UNIT - P_S) // 2,
                                                        BLANK_W + (c+1) * UNIT - (UNIT - P_S) // 2,
                                                        outline='', fill='red')
        #开始画
        self.canvas.pack()
        self.update()


#棋盘类（包括判断当前棋盘输赢的裁判）
class Cboard():
    def __init__(self):
        self.m=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]  #棋盘，蓝方为1，红方为-1，空为0
        self.num_chess=0  #记录当前棋子总数量

    #新开局，可以自定义一个m作为残局开局
    def renew(self, m):
        self.m=m.copy()
        self.num_chess=0

    def getmove(self,x,y,flag): #得到（机器人）指定的点位，以此更新棋盘：x和y为坐标，flag为执蓝还是红
        if self.m[x][y]==1 or self.m[x][y]==-1:
            return -0.5  #犯规，指定点位已经有棋。返回一个大的惩罚-0.5
        else:
            self.m[x][y] = flag
            self.num_chess+=1
            return 0.

    def ref(self):  #裁判，判断目前盘面胜平和僵持（继续走棋），蓝色胜利返回1，红色胜利返回-1，平局返回0，僵持返回100
        #判断每行和每列
        for i in range(3):
            if self.m[i][0]==self.m[i][1]==self.m[i][2]!=0:  #判断行
                return self.m[i][2]
            if self.m[0][i]==self.m[1][i]==self.m[2][i]!=0:  #判断列
                return self.m[2][i]
        #判断左右两个斜线
        if self.m[0][0]==self.m[1][1]==self.m[2][2]!=0:
            return self.m[2][2]
        if self.m[2][0]==self.m[1][1]==self.m[0][2]!=0:
            return self.m[0][2]

        #平局或者僵持
        if self.num_chess>=9:
            return 0  #平局
        else:
            return 100  #表示棋还在僵持中胜负未定，可以继续下







