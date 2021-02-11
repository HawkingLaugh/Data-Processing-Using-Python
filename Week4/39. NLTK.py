from nltk.corpus import gutenberg

# get all contents of gutenberg
contents = gutenberg.fileids()

# count for gutenberg
allwords = gutenberg.words('shakespeare-hamlet.txt')

# all words and punctuations in shakesperae-hamlet
print(len(allwords))

# all unique words in shakesperae-hamlet
print(len(set(allwords)))

allwords.count('Hamlet')

A = set(allwords)
longwords = [w for w in A if len(w) > 12]
print(sorted(longwords))