import pandas as pd
import sqlite3
from scipy.stats import ttest_ind, ttest_1samp

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
df_high_pop_level = pd.read_sql_query(sql_high_pop_query, conn)

#Access the budget for movies with Low popularity level
sql_low_pop_query = f"SELECT {budget_column} FROM joined_table WHERE {popularity_column} = 'Low';"
df_low_popularity_level = pd.read_sql_query(sql_low_pop_query, conn)

#Access movie ratings
sql_vote_average = f"SELECT {vote_average_column} FROM joined_table;"
df_vote_avg = pd.read_sql_query(sql_vote_average, conn)

cursor.close()
conn.close()

# Hypothesis 1: One sample t-test
vote_values = df_vote_avg.values.astype(float)
t_statistic1, p_value1 = ttest_1samp(vote_values, 7)
print(t_statistic1, p_value1)
alpha = 0.05  
if p_value1 < alpha:
    print("Reject the null hypothesis: There is a significant difference between the mean of the vote values and the specified value of 7.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the mean of the vote values and the specified value of 6.44.")


# Hypothesis 2: Two sample t-test
high_pop_array = df_high_pop_level['budget'].values.astype(float)
low_pop_array = df_low_popularity_level['budget'].values.astype(float)
t_statistic2, p_value2 = ttest_ind(high_pop_array, low_pop_array)
print(t_statistic2, p_value2)

alpha = 0.05  
if p_value2 < alpha:
    print("Reject the null hypothesis: There is a significant difference between the budgets of movies with low popularity and high popularity ratings.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the budgets of movies with low popularity and high popularity ratings.")


# Hypothesis 3: Two sample t-test
english_array = df_english_language[vote_average_column].values.astype(float)
non_english_array = df_non_english_language[vote_average_column].values.astype(float)


t_statistic3, p_value3 = ttest_ind(english_array, non_english_array)

print("T-statistic:", t_statistic3)
print("P-value:", p_value3)

alpha = 0.05  
if p_value3 < alpha:
    print("Reject the null hypothesis: There is a significant difference between the average ratings of English and non-English movies.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the average ratings of English and non-English movies.")