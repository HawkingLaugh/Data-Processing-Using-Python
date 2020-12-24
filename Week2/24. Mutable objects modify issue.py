lst = [1,2,4,3,5]
for x in lst:
    if x % 2 == 0:
        lst.remove(x)
print(lst)

# create a shallow copy of the list
for x in lst[:]:
    if x % 2 == 0:
        lst.remove(x)
print(lst)

s = 'beautiful'
for ch in s:
    if ch in "aeiou":
        s = s.replace(ch, '')
print(s)