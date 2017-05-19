import env
import robot
import time

SLEEPTIME=0.1  #休息时间（下慢点方便人类观看）
N_C=1000  #一共下多少盘

show=env.Cshow()
board=env.Cboard()
tom=robot.Crobot(1,1)
jerry=robot.Crobot(-1,0)

n_blue_win=0 #统计蓝色胜利次数
n_red_win=0 #统计红色胜利次数
n_draw=0  #统计平局次数
save_r=[0.]*N_C  #记录每一局的r情况
for C in range(N_C):
    i = 0
    result=100
    board.renew()
    r=0.
    while result==100:

        #Tom下棋
        i += 1
        s=board.m  #记录前一个状态
        x1,y1,flag=tom.move(board.m)
        print(i,'setp : (',x1,y1,')',flag)
        r=board.getmove(x1,y1,flag)
        if r!=0.:
            print('游戏结束（犯规：指定点位已经有棋）')
            break
        show.redraw(board.m)
        result=board.ref()
        if result==1:
            n_blue_win+=1
            r=0.3  #下赢奖励为0.3
            print('蓝棋胜')
            break
        elif result==-1:  #下输了和僵持奖励为0
            n_red_win+=1
            print('红棋胜')
            break
        elif result==0:
            n_draw+=1
            r=0.1  #下平了奖励为0.1
            print('平局')
            break
        time.sleep(SLEEPTIME)

        #Jerry下棋
        i += 1
        x2, y2, flag = jerry.move(board.m)
        print(i,'setp : (',x2,y2,')',flag)
        board.getmove(x2,y2,flag)
        show.redraw(board.m)
        result=board.ref()
        if result==1:
            n_blue_win+=1
            r=0.3  #下赢奖励为0.3
            print('蓝棋胜')
            break
        elif result==-1:
            n_red_win+=1
            print('红棋胜')
            break
        elif result==0:
            n_draw+=1
            r=0.1  #下平了奖励为0.1
            print('平局')
            break
        time.sleep(SLEEPTIME)

    tom.brain_dqn_train.store_transition(s, x1 * 3 + y1, r, board.m)  # 参数分别为(s,a,r,s_)
    if (C > 200) and (C % 5 == 0):
        tom.brain_dqn_train.learn()
    save_r[C]=r
    print('第',C,'幕游戏结束！')
    print('蓝旗胜',n_blue_win,'次:','红棋胜',n_red_win,'次:','平局',n_draw,'次')

print('胜负总览：',save_r)
show.mainloop()