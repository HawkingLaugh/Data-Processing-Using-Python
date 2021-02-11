import numpy as np
from sklearn.cluster import KMeans
listDji = ['MMM', 'AXP', 'AAPL', 'BA','CAT', 'CVX', 'CSCO', 'KO', 'DIS', 'DD']
listTemp = [0] * len(listDji)
# create_df is a self-define function to covert target list into a DF object
for i in range(len(listTemp)):
    listTemp[i] = create_df(listDji[i]).close

status = [0] * len(listDji)

for i in range(len(status)):
    status[i] = np.sign(np.diff(listTemp[i]))
kmeans = KMeans(n_clusters=3).fit(status)
pred = kmeans.predict(status)
print(pred)