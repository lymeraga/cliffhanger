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
revenue_column = 'revenue'
sql_query = f"SELECT {revenue_column} FROM joined_table;"
df_revenue = pd.read_sql_query(sql_query, conn)

#Access the runtime column from our database
runtime_column = 'runtime'
sql_query_two = f"SELECT {runtime_column} FROM joined_table;"
df_runtime = pd.read_sql_query(sql_query_two, conn)

cursor.close()
conn.close()


# Hypothesis 1: Linear regression code
revenue_array = df_revenue[revenue_column].values
runtime_array = df_runtime[runtime_column].values

df = pd.DataFrame({'revenue': revenue_array, 'runtime': runtime_array})
y = df['revenue'].astype(float)  # Dependent variable (revenue)
X = df['runtime'].astype(int)  # Independent variable (runtime)
X = sm.add_constant(X)

model = sm.OLS(y, X)

# Perform the regression
results = model.fit()

# Print regression summary
print(results.summary())
# p_value1 = results.pvalues
# alpha = 0.05  
# if p_value1 < alpha:
#     print("Reject the null hypothesis: There is a significant difference between the budgets of movies with low popularity and high popularity ratings.")
# else:
#     print("Fail to reject the null hypothesis: There is no significant difference between the budgets of movies with low popularity and high popularity ratings.")
