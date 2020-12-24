with open('artical.txt', 'r+') as f:
    p1 = f.readlines()
longestCount = 0
longestWord = ''
for sen in p1:
    senTemp = tuple(sen.split(' '))
    for word in senTemp:
        if '.' in word:
            word = word[:-1]
        if len(word) >= longestCount:
            print(word)
            longestWord = word
            longestCount = len(word)
print("The longest word is {}, it's lenght is {}".format(longestWord,longestCount))

# Sample code
# with open('article.txt') as fp:
#     data = fp.read()
# words = data.split()
# lst = []
# for word in words:
#     if word[-3:] == '...':
#         word = word[:-3]
#         lst.append(word)
#     if word[-1] in ',.?!':
#         word = word[:-1]
#         lst.append(word)
# result = sorted(lst, key = len, reverse = True)
# maxlen = len(result[0])
# # There may be more than one longest word in the article and the words may be same.
# for word in set(result):
#     n = len(word)
#     if n == maxlen:
#         print(word)