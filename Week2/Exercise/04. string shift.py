def move_substr(s, flag, n):
    sLen = len(s)
    if n > sLen:
        return -1
    else:
        if flag == 1:
            return s[n:] + s[:n]
        else:
            return s[-n:] + s[:-n]

if __name__ == "__main__":
    s, flag, n = input('Input the "String,flag,n": ').split(',')
    result = move_substr(s,int(flag),int(n))
    if result != -1:
        print(result)
    else:
        print('Your n is too large')
