#%%
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import scale
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier

wine = pd.read_csv(r'F:\GitHub\Data-Processing-Using-Python\winequality-red.csv', sep = ';')
wine = wine.drop_duplicates()
print(wine.quality.value_counts())

# wine.quality.value_counts().plot(kind = 'pie', autopct = '%.2f')
print(wine.corr().quality)

sns.barplot(x = 'quality', y = 'volatile acidity', data = wine)
sns.barplot(x = 'quality', y = 'alcohol', data = wine)

bins = (2,4,6,8)
group_names = ['low', 'medium', 'high']
wine['quality_lb'] = pd.cut(wine['quality'], bins = bins, labels = group_names)

lb_quality = LabelEncoder()
wine['label'] = lb_quality.fit_transform(wine['quality_lb'])

wine_copy = wine.copy()
wine.drop(['quality', 'quality_lb'], axis=1, inplace=True)
X = wine.iloc[:,:-1]
y = wine.label

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
# scale function to standardize
X_train = scale(X_train)
X_test = scale(X_test)

# Random forest model
# an Ensemble learning algorithm
# = construct and combine multiple learners to finish learning tasks
# Random Forest model = bagging type, representative of parallel ensemble learning

# multiple random sampling to the raw data to acquire multiple different sample sets
# based on each sampling set, training of a decision tree base learners
# followed by combining of these base learners
rfc = RandomForestClassifier(n_estimators= 200)
rfc.fit(X_train, y_train)
y_pred = rfc.predict(X_test)
print(confusion_matrix(y_test, y_pred))

# force search
# search for the best parameters and apply it to the rfc again
param_rfc = {"n_setimartors" : [10,20,30,40,50,60,70,80], "criterion":['gini', 'enttopy']}
grid_rfc = GridSearchCV(rfc, param_rfc, iid=False)
grid_rfc.fit(X_train, y_train)

best_param_rfc = grid_rfc.best_params_

print(best_param_rfc)
rfc = RandomForestClassifier(n_estimators= best_param_rfc)
rfc.fit(X_train, y_train)
y_pred = rfc.predict(X_test)
print(confusion_matrix(y_test, y_pred))