import pandas as pd
import numpy as np
import sqlite3
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, chi2_contingency


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

#Access the rating from the different language column
vote_average_column = 'vote_average'
language_column = 'original_language'
sql_english_language_query = f"SELECT {vote_average_column} FROM joined_table WHERE {language_column} = 'en';"
df_english_language = pd.read_sql_query(sql_english_language_query, conn)

sql_non_eng_query = f"SELECT {vote_average_column} FROM joined_table WHERE {language_column} != 'en';"
df_non_english_language = pd.read_sql_query(sql_non_eng_query, conn)

#Access the budget for movies with High popularity level
budget_column = 'budget'
popularity_column = 'popularity_level'
sql_high_pop_query = f"SELECT {budget_column} FROM joined_table WHERE {popularity_column} = 'High';"
df_english_language = pd.read_sql_query(sql_high_pop_query, conn)

#Access the budget for movies with Low popularity level
sql_low_pop_query = f"SELECT {budget_column} FROM joined_table WHERE {popularity_column} = 'Low';"
df_english_language = pd.read_sql_query(sql_low_pop_query, conn)

cursor.close()
conn.close()



# print(revenue_array)
# print(runtime_array)

# #Hypothesis 1: Linear regression code
# revenue_array = df_revenue[revenue_column].values
# runtime_array = df_runtime[runtime_column].values

# df = pd.DataFrame({'revenue': revenue_array, 'runtime': runtime_array})
# y = df['revenue'].astype(float)  # Dependent variable (revenue)
# X = df['runtime'].astype(int)  # Independent variable (runtime)
# X = sm.add_constant(X)

# model = sm.OLS(y, X)

# # Perform the regression
# results = model.fit()

# # Print regression summary
# print(results.summary())


#Hypothesis 2: Chi Squared Test


# Hypothesis 3: Independent t test
# english_array = df_english_language[vote_average_column].values.astype(float)
# non_english_array = df_non_english_language[vote_average_column].values.astype(float)

# print(english_array)
# print(non_english_array)

# t_statistic, p_value = ttest_ind(english_array, non_english_array)

# print("T-statistic:", t_statistic)
# print("P-value:", p_value)

# alpha = 0.05  
# if p_value < alpha:
#     print("Reject the null hypothesis: There is a significant difference between the average ratings of English and non-English movies.")
# else:
#     print("Fail to reject the null hypothesis: There is no significant difference between the average ratings of English and non-English movies.")