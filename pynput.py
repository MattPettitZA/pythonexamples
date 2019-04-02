# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit

from pynput.mouse import Button, Controller

mouse = Controller()

#move to coordinates
mouse.position = (1500, 200)

#move by amount
mouse.move(150, -130)

#click a button

mouse.click(Button.right, 1)


#press a button
## mouse.press(Button.left)
## mouse.release(Button.left)
#scroll the mouse
##mouse.scroll(0, -100)

