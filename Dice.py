#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Dice.py
#
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit

#
#
import random

def randomnum():
	try:
		sides = int(input("How many sides would you like your die to have?: "))
		num = (random.randint(1,sides))
		print(num)
	except:
		print("Please enter a number")


def main():
	while True:
		randomnum()

main()
