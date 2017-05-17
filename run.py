import env
import robot
import time

SLEEPTIME=1

show=env.Cshow()
board=env.Cboard()
tom=robot.Crobot(1,0)
jerry=robot.Crobot(-1,0)

i=0
result=100
board.renew()
while result==100:

    #Tom下棋
    i += 1
    x,y,flag=tom.move(board.m)
    print(i,"setp : ",x,y,flag)
    board.getmove(x,y,flag)
    show.redraw(board.m)
    result=board.ref()
    if result==1:
        print('蓝棋胜')
        break
    elif result==-1:
        print('红棋胜')
        break
    elif result==0:
        print('平局')
        break
    time.sleep(SLEEPTIME)

    #Jerry下棋
    i += 1
    x, y, flag = jerry.move(board.m)
    print(i,"setp : ",x,y,flag)
    board.getmove(x,y,flag)
    show.redraw(board.m)
    result=board.ref()
    if result==1:
        print('蓝棋胜')
        break
    elif result==-1:
        print('红棋胜')
        break
    elif result==0:
        print('平局')
        break
    time.sleep(SLEEPTIME)

print('游戏结束')

show.mainloop()