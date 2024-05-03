import pandas as pd
import sqlite3
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from statsmodels.tools import eval_measures
from sklearn.metrics import r2_score

db_file_path = '/Users/lyraymeraga/Desktop/cs1951a/final-project-cliffhanger/db_data/Merged_Dataset.db'
conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

#Access the VOTE COUNT column from our database
vote_count_column = 'vote_count'
sql_vote_count_query = f"SELECT {vote_count_column} FROM joined_table"
df_vote_count = pd.read_sql_query(sql_vote_count_query, conn)

#Access the VOTE AVERAGE column from our database
vote_average_column = 'vote_average'
sql_vote_average_query = f"SELECT {vote_average_column} FROM joined_table"
df_vote_average = pd.read_sql_query(sql_vote_average_query, conn)

popularity_level_column = 'popularity_level'

#Access PROFIT column from rows that have high or low popularity_level
filtered_profit_column = 'profit'
sql_filtered_profit_query = f"SELECT {filtered_profit_column} FROM joined_table WHERE {popularity_level_column} = 'High' OR {popularity_level_column} = 'Low';"
df_filtered_profit = pd.read_sql_query(sql_filtered_profit_query, conn)

#Access the POPULARITY column from rows that have high or low popularity_level
filtered_pop_popularity_column = 'popularity'
sql_filtered_popularity_query = f"SELECT {filtered_pop_popularity_column} FROM joined_table WHERE {popularity_level_column} = 'High' OR {popularity_level_column} = 'Low';"
df_filtered_popularity = pd.read_sql_query(sql_filtered_popularity_query, conn)

#Access the VOTE AVERAGE column from rows that have high or low popularity_level
filtered_vote_average_column = 'vote_average'
sql_filtered_vote_average_query = f"SELECT {filtered_vote_average_column} FROM joined_table WHERE {popularity_level_column} = 'High' OR {popularity_level_column} = 'Low';"
df_filtered_vote_average = pd.read_sql_query(sql_filtered_vote_average_query, conn)


#Access the POPULARITY LEVEL column from rows that have high or low popularity_level
sql_high_pop_query = f"SELECT {popularity_level_column} FROM joined_table WHERE {popularity_level_column} = 'High' OR {popularity_level_column} = 'Low';"
df_high_and_low_pop_level = pd.read_sql_query(sql_high_pop_query, conn)

cursor.close()
conn.close()

# Machine Learning 1: Linear regression code
vote_count_array = df_vote_count[vote_count_column].values
vote_average_array = df_vote_average[vote_average_column].values

df = pd.DataFrame({'vote_count': vote_count_array, 'vote_average': vote_average_array})
X = df['vote_count'].astype(float)  # Dependent variable (revenue)
y = df['vote_average'].astype(float)  # Independent variable (budget)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
X = sm.add_constant(X)
X_train = sm.add_constant(X_train)
X_test = sm.add_constant(X_test)

print("values", X_train, X_test, y_train, y_test)
model = sm.OLS(y, X)

# Perform the regression
results = model.fit()

# Print regression summary
print(results.summary())

y_train_pred = results.predict(X_train)
y_test_pred = results.predict(X_test)

mse_train = eval_measures.mse(y_train_pred, y_train)
mse_test = eval_measures.mse(y_test_pred, y_test)

r2 = r2_score(y_test, y_test_pred)
print("r2: ", r2)
print("mse: ", mse_test)

plt.figure(figsize=(10, 6))
plt.scatter(X['vote_count'], y, label='Data Points')
plt.plot(X['vote_count'], results.predict(), color='red', label='Regression Line')
plt.xlabel('vote_count')
plt.ylabel('vote_average')
plt.title('Linear Regression: vote_average vs. vote_count')
plt.legend()
plt.grid(True)
plt.show()


#Machine Learning 2:

df_combined = pd.DataFrame({
    'popularity': df_filtered_popularity[filtered_pop_popularity_column],
    'vote_average': df_filtered_vote_average[filtered_vote_average_column],
    'profit': df_filtered_profit[filtered_profit_column],
    'high_and_low_pop_level': df_high_and_low_pop_level[popularity_level_column]
})

label_encoder = LabelEncoder()
df_combined['high_and_low_pop_level_encoded'] = label_encoder.fit_transform(df_combined['high_and_low_pop_level'])

# Apply one-hot encoding to the encoded target variable
one_hot_encoder = OneHotEncoder(sparse=False)
encoded_labels = one_hot_encoder.fit_transform(df_combined[['high_and_low_pop_level_encoded']])
encoded_labels_df = pd.DataFrame(encoded_labels, columns=['low_encoded', 'high_encoded'])

# Combine the encoded labels with the original DataFrame
df_combined = pd.concat([df_combined, encoded_labels_df], axis=1)

# Splitting the dataset into features and target variable
X = df_combined.drop(['popularity', 'vote_average', 'profit', 'high_and_low_pop_level', 'high_and_low_pop_level_encoded'], axis=1) # Features
y = df_combined['high_and_low_pop_level_encoded']  # Target variable

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing the DecisionTreeClassifier
dt_classifier = DecisionTreeClassifier()

# Training the Decision Tree classifier
dt_classifier.fit(X_train, y_train)

# Making predictions on the testing set
y_pred = dt_classifier.predict(X_test)

# Evaluating the model's accuracy
accuracy = accuracy_score(y_test, y_pred)

print(accuracy)

print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# Map numerical labels to class names
class_names = label_encoder.inverse_transform(dt_classifier.classes_)

# Plot confusion matrix with class names
plt.figure(figsize=(8, 6))
conf_matrix = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=class_names)
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()