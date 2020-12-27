jScore = [9,9,8.5,10,7,8,8,9,8,10]
aScore = 9
# sort by order | sorted(jScore) will not change the contents of original jSocre and have to hold it into another variable
jScore.sort()
# pop the last one(= max after the sort)
jScore.pop()
jScore.pop(0)
jScore.append(aScore)
print(jScore)
average = sum(jScore) / len(jScore)
print(average)