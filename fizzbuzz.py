#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fizzbuzz.py
#
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit

#
#
times = int(input("Please enter the range: "))
numbers = []
def mathversion():

	for i in range(times):

		if (i % 3 == 0) and (i % 5 == 0):
			numbers.append("fizzbuzz")

		elif (i % 3 == 0):
			numbers.append("fizz")

		elif (i % 5 == 0):
			numbers.append("buzz")

		else:
			numbers.append(str(i))
	print(numbers)


def stringversion():
	for i in range(times):
		output = ""
		if i % 3  == 0:
			output += "fizz"

		if i % 5 == 0:
			output += "buzz"

		if output == "":
			output += str(i)

		numbers.append(output)
	print(numbers)

stringversion()
