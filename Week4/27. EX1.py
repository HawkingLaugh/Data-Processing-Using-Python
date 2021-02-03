import pandas as pd

# read the score data in the file score.csv, 
# calculate the average score and 
# count the scores of each course for the students whose Chinese score is 80 or more and 
# English score is 85 or more (sort from big to small), 
# Output the result to the file result.csv and 
# plot a bar chart of the average results of the students who meet the conditions as shown in the figure. 

import pandas as pd
  
df = pd.read_csv('score.csv', index_col = 'Name')
df['Avg'] = (df.Maths+df.Chinese+df.English) // 3
# & represents condition and, that is, both conditions must be met
data = df[(df.Chinese >= 80) & ([1])]    
data = data.sort_values(by = 'Avg', ascending = 0)
data.to_csv('result.csv')
# iloc of this returns a Series
data_parts = data.iloc[:, -1]
# need edit
# data_parts.[2](kind = 'bar')