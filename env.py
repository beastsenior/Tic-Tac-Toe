import tkinter as tk
#import time

BLANK_H = 150 #棋盘上端空白
BLANK_W = 150 #棋盘左端空白
B_H = 3  # 棋盘高
B_W = 3  # 棋盘宽
UNIT = 90  # 棋盘每格大小
P_S = 60 #棋子大小

class Cenv(tk.Tk):
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
        ##开始监听鼠标左键.
        #self.canvas.bind('<Button-1>', self.OnB1)

    #def check(self,m):
