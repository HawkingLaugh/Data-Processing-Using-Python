import string
alphabetList = list(string.ascii_lowercase)

def countchar(x):
    lst = [0] * 26
    for i in range(len(x)):
        # confirm number only
        if x[i] >= 'a' and x[i] <= 'z':
            # ord function to get the value of the alphabet a = 97 b = 98 c = 99.
            # from finding the different between value of x[i] and 'a', to get the index(if b, 98 - 97 = 1 = [1]) in lst and add 1 into the index position
            lst[ord(x[i]) - ord('a')] += 1
    print(lst)

if __name__ == "__main__":
    s = "Hope is a good thing."
    s = s.lower()
    countchar(s)