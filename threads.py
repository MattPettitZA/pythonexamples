#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  threads.py
#
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit
#
#
#
# taken from: https://www.youtube.com/watch?v=WhtUuZLOo00

import threading
mainlist = []

def runner(num):
	mainlist.append("url:"+str(num))

threads = []

for i in range(10):
	t = threading.Thread(target=runner,args=(i,))
	threads.append(t)
	t.start()
print(mainlist)
