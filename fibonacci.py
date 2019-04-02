import time
x =  int(input('Number of numbers: '))

num = []
firstnum = 0
secondnum = 1
starttime = time.time()
for i in range(x):
    answer = firstnum+secondnum
    firstnum = secondnum
    secondnum = answer
    num.append(secondnum)
print(secondnum)
endtime =time.time()
timetook = endtime - starttime
print('Generated '+str(x)+' numbers.')
print('Took '+str(timetook))
