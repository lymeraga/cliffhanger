Data Deliverable

Data Spec:

ID:
Type of Data: primary key and integer 
Default Value: No default value each id is unique
Range of Values: 100 - 320,000
Distribution: It is unique for each record if it serves as a primary key.
Uniqueness: Each id is different and unique
Duplicate Detection: There are no duplicates that exist
Required Value: Yes, IDs are required for uniquely identifying records.
Usage in Analysis: IDs are being used as primary keys in our database
Sensitivity: IDs don't contain sensitive information.

Popularity:
Type of Data: Floating-point number 
Default Value: The median value is 5 but the default is 0
Range of Values: Between 0 and 10
Distribution: Skewed and unevenly distributed. The majority of movies have a rating from 0-4.
Uniqueness: Popularity values can repeat, but since they are real values almost all are unique
Duplicate Detection: No exact decimal duplicates however, if rounded there are several
Required Value: Yes
Usage in Analysis: Used to understand the popularity trends of items, will most likely compare with vote_count
Sensitivity: Not sensitive only number values

Budget:
Type of Data: Floating-point representing monetary values
Default Value: 0 
Range of Values: Positive numeric values representing currency amounts.100,000 - 99,000,000
Distribution: Relatively normal distribution heavier distribution on lower values
Uniqueness: Budget values do repeat
Duplicate Detection: Budget values do repeat
Required Value: Yes
Usage in Analysis: Interesting to analyze the movies budget with how well liked the movie was. As well as the increase in movies budgets over the year they were released.
Sensitivity: Not sensitive 

Cast:
Type of Data: List of strings representing the cast members.
Default Value: Empty string
Range of Values: Names of actors and cast members.
Distribution: Varies widely depending on the number of cast members per item.
Uniqueness: Cast combinations could repeat across different items.
Duplicate Detection: Definitely multiple movies that contained one or two actors in common  
Required Value: Yes
Usage in Analysis: Analyze how the number of actors was correlated with the movie price
Sensitivity: Not sensitive 

Genres:
Type of Data: List of strings representing the genres.
Default Value: Empty string
Range of Values: Various genres such as action, comedy, drama, etc.
Distribution: Good diversity of different genres.
Uniqueness: Genre combinations repeat across movies. Almost all movies stem from one of ten genres
Duplicate Detection: Genres alone might not be sufficient for detecting duplicates.
Required Value: Yes
Usage in Analysis: Analyze the genre of the movie with budget as well as the popularity level
Sensitivity: Not sensitive 

Release Year:
Type of Data: Integer representing the release year.
Default Value: 0
Range of Values: Range from 1961 - 2015
Distribution: Much more heavily concentrated in the years starting after 2000
Uniqueness: Release years repeat across different items.
Duplicate Detection: Multiple movies produced in the same year
Required Value: Yes
Usage in Analysis: Explore the relationship between release year and financial performance metrics such as box office revenue, budget, and profit.
Sensitivity: Not sensitive

Profit:
Type of Data: Float representing monetary values
Default Value: 0
Range of Values: Positive and negative values representing currency amounts ranging from 10,117,423 to 99,272,124 
Distribution: Varies widely depending on the profitability of items.
Uniqueness: Profit values could repeat across different items.
Duplicate Detection:  No exact decimal duplicates however if rounded there are several
Required Value: Yes
Usage in Analysis: Analyze whether certain genres consistently yield higher profits or if profitability varies depending on other factors such as production budget or marketing strategy
Sensitivity: Not sensitive 

Original Language:
Type of Data: Two letter string combination represent the abbreviated language
Default Value: Empty string
Range of Values: Various languages such as English, Spanish, French, etc.
Distribution: 95% english
Uniqueness: Original language values repeat across different items.
Duplicate Detection: All dataset items are one of around five languages
Required Value: yes
Usage in Analysis: Develop language-based recommendation systems for movie enthusiasts
Sensitivity: Not sensitive 

Concise Tech Report

How many data points are there in total? How many are there in each group you care about (e.g. if you are dividing your data into positive/negative examples, are they split evenly)?: There are 1106 rows and 23 columns giving us a total of 25,438 data points. Our data is completely populated meaning there are 23 data points per each movie.
Aim for a resource of reasonable size. At least 700 records after cleaning and duplicate removal. Account that part of your data should be used for validation of your results only.: We have over 700 records after cleaning.
Do you think this is enough data to perform your analysis later on?: We believe that this is more than enough data to perform analysis later on because we include a wide range of movies with varying popularities, genres, runtimes, production companies, release dates, profits, original languages, etc. meaning that we can test many different hypotheses with statistical significance.
What are the identifying attributes?: The identifying attributes of our dataset are a movie’s TMDB id, popularity, budget, revenue, original title, cast, director, tagline, keywords, overview, runtime, genres, production company, release date, vote count, vote average, release year, budget adjusted for inflation, revenue adjusted for inflation, profit, popularity level, original language, and whether the movie is adult rated.
Where is the data from?
How did you collect your data?: We collected our data from 3 separate datasets found on Kaggle which come from scraping the TMDB Movie Database.
Is the source reputable?: The source is reputable because it comes from TMDB which is used widely for movie analysis and controlled for quality.
How did you generate the sample? Is it comparably small or large? Is it representative or is it likely to exhibit some kind of sampling bias?: The sample of our data that we provided was generated by taking the first 100 rows of our dataset. This is relatively small compared to the 1106 rows that we have in total. This sample has the potential to exhibit some sort of sampling bias if our first 100 rows come from one of the Kaggle datasets that listed top rated movies while our other datasets that we joined are generic (not ordered based on rating). However, when considering our entire merged dataset, this should be less prevalent. 
Are there any other considerations you took into account when collecting your data? This is open-ended based on your data; feel free to leave this blank. (Example: If it's user data, is it public/are they consenting to have their data used? Is the data potentially skewed in any direction?): N/A

Our team has worked to ensure that our data is clean and complete. It includes information that will help us investigate and test our hypothesis.
To check for cleanliness of data we removed duplicate columns to ensure each unique information only appeared once. So for example, each of the three movie databases we wanted to join had a column representing the movie title. Since they represented the same information we chose to only keep one of the columns and dropped the other two. Our threshold reference was removal of duplicate entries and ensuring there was no missing values.
As part of our data cleaning process, we used SQL queries mainly to remove unnecessary columns. Specifically, we used “ALTER TABLE” to drop columns that were redundant.
We were careful to choose databases that did not have any missing values to ensure that we can reach our project’s goals.
The data distribution depends on the type of data. This information can be found in the data spec above.
We examined each column in the dataset to ensure that the data type matches the expected type.
We kept all the data that was not redundant. However, if we already had some information from one database and the same information was represented in another database, we decided to throw away redundant data. This does not affect any conclusions we are going to be able to draw from our data. 

One observation we have made by collecting data is data redundancy. We have observed instances where duplicate records exist with the dataset, potentially affecting our analysis outcomes and hypothesis testing process. During our data cleaning process we identified and eliminated these duplicate entries, ensuring that each data point is represented accurately. The analysis we will perform remains the same as stated in the group project proposal since we have data that will allow us to test our hypothesis.




HYPOTHESIS 1

Why did you use this statistical test or ML algorithm? 
We used a one-sample t-test to test this hypothesis because we wanted to compare the sample mean with our estimated population mean.

Which other tests did you consider or evaluate?
We were able to identify this test as the best fit for this hypothesis from the beginning because it only involves one sample.

What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? 
We used the p-value to determine the statistical significance of the difference in the sample mean and our target value. If the p-value is less than the chosen significance level (e.g., alpha = 0.05), we reject the null hypothesis, indicating a significant difference between the two values. 
One challenge that we faced when evaluating the model was choosing a semi arbitrary mean to compare our data against.

Did you have to clean or restructure your data?
We used a sql query to access only the vote_average column from our database.

What is your interpretation of the results? 
Seeing as our p-value was calculated to be 6.34953111e-133, we reject the null hypothesis, meaning there is a significant difference between the mean of the vote values and the specified value of 7.

Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy?
We deny the hypothesis which makes sense because we calculated the actual mean of this column to be 6.44.

For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? 
We predicted that the mean vote for this set of movies would be 7 because, but we weren’t too surprised to find out that in reality it was a bit lower.

Are you confident in the results?
Given the statistical significance and rigorous methodology applied, I am confident in the obtained results and their implications regarding the mean of the vote averages for these movies

HYPOTHESIS 2
Why did you use this statistical test or ML algorithm? 
The two-sample t-test was chosen to compare the means of two independent groups (movies with high popularity vs. low popularity) in terms of their budgets. This test helps assess whether the difference in means between these groups is statistically significant.The t-test is suitable for comparing means of continuous variables (budget in this case) across two groups (high and low popularity ratings).

Which other tests did you consider or evaluate? 
We were also considering using the one-sample t-test. In that case, we would compare the mean of the budgets for movies high popularity with the budgets for all the movie in the dataset. 

What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? 
We used the p-value to determine the statistical significance of the observed difference in means between high and low popularity groups. If the p-value is less than the chosen significance level (e.g., alpha = 0.05), we reject the null hypothesis, indicating a significant difference between groups. 
One challenge that we faced is that for statistical tests like the t-test, it's crucial to validate assumptions such as normality and homogeneity of variances between groups. 

Did you have to clean or restructure your data?
Yes, we had to clean the data to ensure data compatibility for statistical analysis. We did this using the following sql queries: “SELECT {budget_column} FROM joined_table WHERE {popularity_column} = 'High'; and SELECT {budget_column} FROM joined_table WHERE {popularity_column} = 'Low';” That way the two values that we wanted to test in our model were only the select columns.

What is your interpretation of the results? 
The significant p-value (5.3278058737316e-32) from the t-test indicates strong evidence against the null hypothesis, suggesting that there is a meaningful difference in budgets between movies with high and low popularity ratings.  This finding implies that movie studios or producers may allocate higher budgets to movies expected to be more popular, likely due to anticipated higher returns or the need for larger-scale production to attract audiences.

Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy?
Based on the results of the two-sample t-test (significant p-value), we reject the null hypothesis and accept the alternative hypothesis that there is a significant difference in budgets based on movie popularity ratings.

For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? 
The results align intuitively with industry knowledge and common sense. It is logical to expect that movies with higher anticipated popularity would receive larger budgets to support marketing efforts, star castings, visual effects, and overall production quality.

Are you confident in the results?
Given the statistical significance and rigorous methodology applied, I am confident in the obtained results and their implications regarding the relationship between movie budgets and popularity ratings.

HYPOTHESIS 3
Why did you use this statistical test or ML algorithm?
A two-sample t-test is used here because it's suitable for comparing the means of two independent samples, which is precisely what's needed to evaluate the hypothesis that movies released in English have higher average ratings compared to movies released in other languages. 

Which other tests did you consider or evaluate?
We were also considering using the one-sample t-test. In that case, we would compare the mean of the votes for movies in English with the vote average of all movies in the dataset. 

What metric(s) did you use to measure success or failure, and why did you use it?
The primary metric used here is the p-value. A p-value less than 0.05 indicates that the null hypothesis can be rejected, suggesting a significant difference between the groups. A higher p-value suggests that there is insufficient evidence to conclude a significant difference.

What challenges did you face evaluating the model?
One thing we had to be careful about was ensuring that the assumptions of the t-test were met, such as the normality of the data.

Did you have to clean or restructure your data?
We restructured the data to only include data of our interest using queries:
#Access the rating from the different language column
vote_average_column = 'vote_average'
language_column = 'original_language'
sql_english_language_query = f"SELECT {vote_average_column} FROM joined_table WHERE {language_column} = 'en';"
df_english_language = pd.read_sql_query(sql_english_language_query, conn)
sql_non_eng_query = f"SELECT {vote_average_column} FROM joined_table WHERE {language_column} != 'en';"
df_non_english_language = pd.read_sql_query(sql_non_eng_query, conn)

What is your interpretation of the results?
The p-value 0.539 is higher than the significance level of 0.05, indicating that there is insufficient evidence to reject the null hypothesis. Therefore, based on this analysis, there is no significant difference between the average ratings of English and non-English movies.

Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy?
Given the result, the hypothesis that movies released in English have higher average ratings compared to movies released in other languages is not supported by the data. However, it's essential to note that lack of significance doesn't necessarily mean the hypothesis is false; it could be due to various factors such as sample size, variability within groups, or other unaccounted variables.

For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results?
The result suggests that language alone might not be a significant factor in determining movie ratings. Other factors such as genre, marketing, and cultural relevance could play a more substantial role. It's intuitive that while language might affect the accessibility of a movie to a particular audience, it doesn't inherently determine its quality or audience reception.

Are you confident in the results?
Given that our data is of good quality and we have used an appropriate statistical test, we are pretty confident in our results. 



Machine Learning 1
Why did you use this statistical test or ML algorithm? 
Linear regression was chosen because it is well-suited for modeling the relationship between two continuous variables (movie budget and movie revenue) and quantifying the strength and direction of this linear relationship. The objective was to understand how changes in movie budgets (independent variable) impact movie revenues (dependent variable) based on historical data.

Which other tests did you consider or evaluate? 
We though about other machine learning algorithms like decision trees or random forests but we decided to use a more simple and concise modeling of the relationship.
W
hat metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? 
We used two metrics to measure the success or failure of our model. The R-squared coefficient is used to measure the proportion of variance in the dependent variable (movie revenue) that is explained by the independent variable (movie budget). A higher R-squared value indicates a better fit of the model to the data. The Mean Squared Error (MSE) is used to quantify the average squared difference between predicted and actual values of movie revenue. Lower MSE values indicate better predictive performance.
The main challenges we faced were ensuring model assumptions like linearity, independence, homoscedasticity are met. As well as examining influential data points that could skew the regression results.

Did you have to clean or restructure your data?
We restructured the data to only include data of our interest using SQL queries:
#Access the VOTE COUNT column from our database
vote_count_column = 'vote_count'
sql_vote_count_query = f"SELECT {vote_count_column} FROM joined_table"
df_vote_count = pd.read_sql_query(sql_vote_count_query, conn)
#Access the VOTE AVERAGE column from our database
vote_average_column = 'vote_average'
sql_vote_average_query = f"SELECT {vote_average_column} FROM joined_table"
df_vote_average = pd.read_sql_query(sql_vote_average_query, conn)

What is your interpretation of the results? 
The R-squared value of 0.230 indicates that approximately 23.0% of the variability in movie ratings (vote_average) can be explained by variations in vote_count (number of votes or popularity).This suggests a moderate level of predictive power in the model, indicating that while movie popularity (as measured by vote count) contributes to rating variability, there are other factors not captured by the model.
Vote Count (vote_count): The coefficient of 0.0002 suggests that, on average, each additional vote (increase in popularity) is associated with an increase of 0.0002 in the movie rating (vote_average).
The p-values (P>|t|) for both intercept and vote count are very low (close to 0), indicating that they are statistically significant predictors of movie ratings at the conventional significance level (alpha = 0.05).

Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy?
Based on the statistically significant coefficient for vote_count and the overall R-squared value, we can conclude that there is a positive relationship between movie popularity (vote count) and movie ratings (vote_average).
The model explains a decent amount of variability in movie ratings based on popularity, but additional factors beyond vote count likely influence audience ratings.

For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? 
The results suggest that audience engagement (measured by vote count) does have a positive impact on movie ratings, which aligns with common intuition in the film industry.However, the model's R-squared of only 0.230 indicates that other factors, such as plot, acting, and production quality, also play significant roles in determining movie ratings.

Are you confident in the results?
We are slightly confident in our result. The model statistics and significant coefficients and suggest that the relationship between vote count and movie ratings is meaningful and supported by the data.
However we are limited because the high condition number which indicates potential multicollinearity  and moderate R-squared value highlight potential areas for improvement our model specification and feature selection.

Machine Learning 2
Why did you use this statistical test or ML algorithm?
In this case we use the Decision Tree Classifier (DT) because it can handle categorical data and it is useful for classification. Our target variable is a categorical one which has values of either low or high. Based on certain movie features such as vote average and profit we wanted to determine the popularity level of the movie.

Which other machine learning model did you consider or evaluate?
We also considered using Support Vector Machine since they are effective in categorical classification. Given a set of labeled training data, SVM aims to find the line that best separates the different classes in the feature space. This line, called the hyperplane, is then used to classify new, unlabeled data points into one of the predefined classes.

What metric(s) did you use to measure success or failure, and why did you use it?
The metric used to measure the model's performance is accuracy, calculated using the accuracy_score function. Accuracy is a suitable metric for balanced datasets where each class is equally important. It measures the proportion of correctly predicted labels over the total number of predictions. 

What challenges did you face evaluating the model?
We had to ensure that the features we were using were of equal importance and affected the decision making process in a similar way. 

Did you have to clean or restructure your data?
Yes, we encoded categorical variables using LabelEncoder and OneHotEncoder and split the dataset into training and testing sets.

What is your interpretation of the results?
The accuracy score provides a measure of how well the decision tree model predicts the target variable. The classification report and confusion matrix offer additional insights into the model's performance. We did not get any false positives or false positives which meant that our model was trained well.

Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy?
We are quite satisfied with the prediction accuracy of our decision tree since it always classified the popularity level of the movie accurately.

For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results?
The accuracy achieved by the decision tree model reflects how well it generalizes to unseen data. Since our accuracy is high, it suggests that the model can effectively distinguish between the classes based on the provided features.

Are you confident in the results?
Since our data was of good quality and our decision tree model had a high accuracy score, we are confident in the results we got.


OTHER
Did you find the results corresponded with your initial belief in the data? If yes/no, why do you think this was the case?
We generally found that the results corresponded with our initial beliefs in the data, however, there were also results that surprised us. We expected there to be a statistically significant difference in budgets between movies with high and low popularity ratings because we believed that the budget of a movie likely played a major role in its success, which proved to be correct. We expected the popularity score, profit, and vote average to be determinants of popularity level which proved to be correct, as our decision tree trained on these attributes was extremely accurate. We expected there to be a correlation between vote count and vote average because we assumed people would be more likely to voluntarily rate a movie if they had a more positive opinion on it, which seems to hold loosely according to our regression. We expected movies released in English to have higher average ratings compared to movies released in other languages, but there was not enough evidence to reject the null hypothesis that there is no significant difference in the average ratings of English and non-English movies. We also expected the mean of the vote averages to be around 7 which was slightly off according to our hypothesis testing.

Do you believe the tools for analysis that you chose were appropriate? If yes/no, why or what method could have been used?
We believe the tools for analysis that we chose were appropriate because they provided meaningful results that we were able to interpret both statistically and intuitively. For example, when trying different types of regression to see what model would fit our data best, we settled on linear regression even though it is not a perfect fit because it follows the general trend in a way that is easy to follow for our audience.

Was the data adequate for your analysis? If not, what aspects of the data were problematic and how could you have remedied that?
The data we used was adequate for all the hypothesis tests and machine learning algorithms we wanted to run. One aspect of the data that was problematic was that many of the columns had words rather than numerical values which were harder for us to work with, so we generally avoided those features. With more time, we could have remedied this by further cleaning our data to convert many of these verbal descriptions to binary columns that we could work with in our analysis. However, we are happy with the results we were able to pull from the numerical columns. 
