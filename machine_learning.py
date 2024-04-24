import pandas as pd
import numpy as np
import sqlite3
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, ttest_rel, ttest_1samp


db_file_path = '/Users/lyraymeraga/Desktop/cs1951a/final-project-cliffhanger/db_data/Merged_Dataset.db'
conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

#Acess the revenue from our database
vote_count_column = 'vote_count'
sql_vote_query = f"SELECT {vote_count_column} FROM joined_table;"
df_vote_count = pd.read_sql_query(sql_vote_query, conn)

#Access the budget column from our database
vote_average_column = 'vote_average'
sql_query_two = f"SELECT {vote_average_column} FROM joined_table;"
df_vote_average = pd.read_sql_query(sql_query_two, conn)

cursor.close()
conn.close()

# Machine Learning 1: Linear regression code
vote_count_array = df_vote_count[vote_count_column].values
vote_average_array = df_vote_average[vote_average_column].values

df = pd.DataFrame({'vote_count': vote_count_array, 'vote_average': vote_average_array})
X = df['vote_count'].astype(float)  # Dependent variable (revenue)
y = df['vote_average'].astype(float)  # Independent variable (budget)
X = sm.add_constant(X)

model = sm.OLS(y, X)

# Perform the regression
results = model.fit()

# Print regression summary
print(results.summary())

plt.figure(figsize=(10, 6))
plt.scatter(X['vote_count'], y, label='Data Points')
plt.plot(X['vote_count'], results.predict(), color='red', label='Regression Line')
plt.xlabel('vote_count')
plt.ylabel('vote_average')
plt.title('Linear Regression: vote_average vs. vote_count')
plt.legend()
plt.grid(True)
plt.show()