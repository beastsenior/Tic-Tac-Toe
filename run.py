import env
import robot

show=env.Cshow()
board=env.Cboard()
bot_tom=robot.Crobot()
bot_jerry=robot.Crobot()

board.renew()
x,y,flag=bot_tom.move(board.m)
board.getmove(x,y,flag)

print(board.m)
show.redraw(board.m)


show.mainloop()