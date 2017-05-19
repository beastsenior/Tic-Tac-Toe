import env
import robot
import time

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.ion()
plt.show()

SLEEPTIME=0  #休息时间（下慢点方便人类观看）
N_C=20000  #一共下多少盘

show=env.Cshow()
board=env.Cboard()
tom=robot.Crobot(1,1)
jerry=robot.Crobot(-1,0)

r_sum_time=20
r_sum=0
x_values = []
y_values = []


n_blue_win=0 #统计蓝色胜利次数
n_red_win=0 #统计红色胜利次数
n_draw=0  #统计平局次数
save_r=[0.]*N_C  #记录每一局的r情况

for C in range(N_C):
    #画图
    if C % r_sum_time == 0 and C!=0:
        x_values.append(C/r_sum_time)
        y_values.append(r_sum)
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        lines = ax.plot(x_values, y_values, 'r-', lw=1)
        r_sum=0
        #plt.pause(1)

    #下棋
    tom.brain_dqn_train.epsilon = 0.1+ C / N_C
    if tom.brain_dqn_train.epsilon>=1.0:
       tom.brain_dqn_train.epsilon=1.0
    # if C>7000:
    #     tom.brain_dqn_train.epsilon = 0.8
    i = 0
    result=100
    board.renew([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    print('board.renew',board.m)
    r=0.
    end_flag=False  #判断棋局是否结束
    show.redraw(board.m)
    while result==100:
        #Tom下棋
        i += 1
        s=tom.brain_dqn_train.m2s(board.m)  #记录前一个状态
        x1,y1,flag=tom.move(s)
        print(i,'setp : (',x1,y1,')',flag)
        r=board.getmove(x1,y1,flag)
        if r!=0.:
            n_red_win += 1
            print('游戏结束（犯规：指定点位已经有棋）')
            end_flag=True
        else:
            show.redraw(board.m)
            result=board.ref()
            if result==1:
                n_blue_win+=1
                r=0.3  #下赢奖励为0.3
                print('蓝棋胜')
                end_flag=True
            elif result==-1:  #下输了和僵持奖励为0
                n_red_win+=1
                print('红棋胜')
                end_flag = True
            elif result==0:
                n_draw+=1
                r=0.1  #下平了奖励为0.1
                print('平局')
                end_flag = True
            time.sleep(SLEEPTIME)

        if end_flag==False:
            #Jerry下棋
            i += 1
            s_tmp = tom.brain_dqn_train.m2s(board.m)
            x2, y2, flag = jerry.move(s_tmp)
            print(i,'setp : (',x2,y2,')',flag)
            board.getmove(x2,y2,flag)
            show.redraw(board.m)
            result=board.ref()
            if result==1:
                n_blue_win+=1
                r=0.3  #下赢奖励为0.3
                print('蓝棋胜')
                end_flag = True
            elif result==-1:
                n_red_win+=1
                print('红棋胜')
                end_flag = True
            elif result==0:
                n_draw+=1
                r=0.1  #下平了奖励为0.1
                print('平局')
                end_flag = True
            time.sleep(SLEEPTIME)

        tom.brain_dqn_train.store_transition(s, x1 * 3 + y1, r, tom.brain_dqn_train.m2s(board.m))  # 参数分别为(s,a,r,s_)
        if (C > 200) and (C % 5 == 0):
            tom.brain_dqn_train.learn()
        if end_flag==True:
            r_sum+=r
            save_r[C]=r
            print('第',C+1,'幕游戏结束！')
            print('蓝旗胜',n_blue_win,'次:','红棋胜',n_red_win,'次:','平局',n_draw,'次')
            break

print('胜负总览：',save_r)
show.mainloop()