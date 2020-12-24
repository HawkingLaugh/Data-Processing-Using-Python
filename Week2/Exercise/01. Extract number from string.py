#  For the string = 'My moral standing  is: 0.98765', please extract the number string and print its float data.
string = 'My moral standing  is: 0.98765'
# split the string into 2 parts by : and take the second part only
moralStr = string.split(':')[1]
result = float(moralStr)
print(result)