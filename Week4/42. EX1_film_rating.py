import pandas as pd
import numpy as np

# as both of the raw files didn't come with heading and names, add names manually
# can access location by iloc or indexing by loc
# df.loc[:, ['attA', 'attB]]
# pd.read_csv(header = None) to avoid reading the original title(if any) as a row of data
unames = ['user id', 'age', 'gender', 'occupation', 'zip code']
users = pd.read_csv('ml-100k/u.user', sep = '|', names=unames)

rnames = ['user id', 'item id', 'rating', 'timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names = rnames)

users_df = users.loc[:, ['user id', 'gender']]
ratings_df = ratings.loc[:, ['user id', 'rating']]
# 100K rows of data with 3 columns(user id, gender, rating)
ratings_df = pd.merge(users_df, ratings_df)

# using the std from pd Series due to the denominator is n-1 instead of n
# n-1 no non-bias
# ratings_df.groupby('gender').rating.apply(pd.Series.std)

ratings_df.groupby('gender').rating.std()

# adjust the bias from single users by calculating the mean of each user first
# df.groupby([attA, attB]) accept multiple attributes 
# 943 rows and 1 row for each user
user_avg = ratings_df.groupby(['user id', 'gender']).apply(np.mean)

print(user_avg.groupby('gender').rating.std())

pd.pivot_table(user_avg, values = 'rating', index = 'gender', aggfunc = pd.Series.std)

# default aggfunc = mean
pivot_mean = pd.pivot_table(ratings_df, index = ['user id','gender'], values = 'rating')
female = pivot_mean.query("gender == ['F']")
female = pivot_mean.query("gender == ['M']")
f_std = pd.Series.std(female)
print(f_std)