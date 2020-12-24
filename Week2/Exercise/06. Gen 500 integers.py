"""
Use random function to generate 500 integers in the range of 1-100, 
store them into a file called random.txt, one number in each line. 
Program to find out the mode and print it ( the definition of mode is the number which appears the most times).
"""
import random    
with open('random.txt', 'w+') as f:
    for i in range(500):
        f.write(str(random.randint(1, 100)))
        f.write('\n')
    f.seek(0)
    nums = f.readlines()
countList = [0] * 101
setNums = set(nums)
for num in setNums:
    c = nums.count(num)
    countList[int(num)] = c
for i in range(len(countList)):
    if countList[i] == max(countList):
        print("The mode is {} for appearing {} times".format(i,countList[i]))