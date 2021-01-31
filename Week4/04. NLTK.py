from nltk.corpus import gutenberg
import nltk

text = gutenberg.words('shakespeare-hamlet.txt')
print(text)