# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit

#working

f = open("Output.txt", "w")

input1 = input("What would you like to paste in?: ")

f.write(input1)
f.write("\nWritten in Python by magical bot bro")


f.close()
