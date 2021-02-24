#%% 
from nltk.corpus import stopwords
from nltk.corpus import brown
import nltk
from nltk.inference.tableau import Categories

stopwords = stopwords.words('english')
# if words not in stopwords:
#     ...

# brown handles conditional frequency distribution

# specific the category of news
print(brown.words(categories = 'news'))

# identifier of 'ca16
print(brown.words(fileids = 'ca16'))

# Modal verbs

cfd = nltk.ConditionalFreqDist((genre, word) for genre in brown.categories() for word in brown.words(categories = genre))

genres = ['news', 'romance']
modals = ['can', 'could', 'may', 'might', 'must', 'will', 'would']

cfd.tabulate(conditions=genres, samples=modals)
cfd.plot(conditions = genres, samples = modals)


# %%
