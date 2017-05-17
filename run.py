import env
import robot

show=env.Cshow()
board=env.Cboard()
bot_tom=robot.Crobot()
bot_jerry=robot.Crobot()

temp= [[0,0,0],
                [0,0,0],
                [0,0,1]]
board.renew(temp)
show.redraw(board.m)


show.mainloop()