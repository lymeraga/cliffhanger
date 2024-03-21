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
