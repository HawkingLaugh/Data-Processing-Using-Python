# twonums_sum returns the index of the nums inside the list that can become n
def twonums_sum(n, lst):
     d = {}
     for i in range(len(lst)):
          d[lst[i]] = i    # create number-subscript pair
     for i in range(len(lst)):
          if n - lst[i] in d:
               return i, d[n-lst[i]]
     return -1


lst = [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 19, 20, 21, 29, 34, 54, 65]
n = int(input())
result = twonums_sum(n, lst)
if result == -1:
    print("not found")
else:
    print(result)
