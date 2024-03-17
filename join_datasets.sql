ATTACH DATABASE '/Users/francescaelia/Documents/cs1951a/final-project-cliffhanger/db_data/TMBD_Movies_Dataset_2.db' AS db2;
ATTACH DATABASE '/Users/francescaelia/Documents/cs1951a/final-project-cliffhanger/db_data/TMBD_Movies_Dataset_3.db' AS db3;

DROP TABLE IF EXISTS joined_table;
CREATE TABLE joined_table AS
SELECT *
FROM main.table_1 AS t1
INNER JOIN db2.table_2 AS t2 ON t1.id = t2.id
INNER JOIN db3.table_3 AS t3 ON t1.id = t3.id
GROUP BY t1.id;

ALTER TABLE joined_table
DROP COLUMN unknownColumn, imdb_id, homepage;

ALTER TABLE joined_table
DROP COLUMN unknownColumn;
ALTER TABLE joined_table
DROP COLUMN imdb_id;
ALTER TABLE joined_table
DROP COLUMN homepage;
ALTER TABLE joined_table
DROP COLUMN "unknownColumn:1";
ALTER TABLE joined_table
DROP COLUMN "id:1";
ALTER TABLE joined_table
DROP COLUMN "original_title:1";
ALTER TABLE joined_table
DROP COLUMN "overview:1";
ALTER TABLE joined_table
DROP COLUMN "popularity:1";
ALTER TABLE joined_table
DROP COLUMN "release_date:1";
ALTER TABLE joined_table
DROP COLUMN title;
ALTER TABLE joined_table
DROP COLUMN "vote_average:1";
ALTER TABLE joined_table
DROP COLUMN "vote_count:1";
ALTER TABLE joined_table
DROP COLUMN "unknownColumn:2";
ALTER TABLE joined_table
DROP COLUMN "id:2";
ALTER TABLE joined_table
DROP COLUMN "title:1";
ALTER TABLE joined_table
DROP COLUMN "original_language:1";
ALTER TABLE joined_table
DROP COLUMN "release_date:2";
ALTER TABLE joined_table
DROP COLUMN "vote_average:2";
ALTER TABLE joined_table
DROP COLUMN "popularity:2";