import tkinter as tk
#import time

BLANK_H = 150 #棋盘上端空白
BLANK_W = 150 #棋盘左端空白
B_H = 3  # 棋盘高
B_W = 3  # 棋盘宽
UNIT = 90  # 棋盘每格大小
P_S = 60 #棋子大小

class Cshow(tk.Tk):
    def __init__(self):
        super(Cenv, self).__init__()
        self.title('井字棋')
        self.geometry('{0}x{1}'.format(600, 600))
        self.redraw([[0,0,0],
                     [1,0,0],
                     [1,-1,0]])

    def redraw(self,m):
        try:
            self.canvas.delete("all")  #清空画布
        except:
            pass

        #画布
        self.canvas = tk.Canvas(self, bg='white', height=600, width=600)
        #棋盘
        for c in range(BLANK_W, BLANK_W+(B_W+1)* UNIT, UNIT):
            x0, y0, x1, y1 = c, BLANK_H, c, BLANK_H+B_H* UNIT
            self.canvas.create_line(x0, y0, x1, y1,width=2)
        for r in range(BLANK_H, BLANK_H+(B_H+1)* UNIT, UNIT):
            x0, y0, x1, y1 = BLANK_W, r, BLANK_W+B_W* UNIT, r
            self.canvas.create_line(x0, y0, x1, y1,width=2)
        #棋子
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

    #def check(self,m):

#棋盘类（包括判断当前棋盘输赢的裁判）
class Cboard():
    def __init__(self):
        self.m=[[0,0,0],
                [0,0,1],
                [0,-1,-1]]  #棋盘，蓝方为1，红方为-1，空为0
        self.num_chess=0  #记录当前棋子总数量

    #新开局
    def renew(self):
        self.m=[[0,0,0],
                [0,0,0],
                [0,0,0]]

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
        if self.num_chess==9:
            return 0
        else:
            return 100







