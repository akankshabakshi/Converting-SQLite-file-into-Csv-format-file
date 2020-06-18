#Importing useful libraries:
import pandas as pd
import sqlite3

#Build connection with Sqlite:
conn = sqlite3.connect('/Users/akankshabakshi/database.sqlite')

#Print all tables query:
sql = "select * from sqlite_master where type = 'table';"

#Read all table query using pandas: 
df = pd.read_sql_query(sql, conn);

#View all data in the sqlite file:
df

#SQL query for league table:
sql_1 = """select * from league;"""

#Read league table using pandas:
df_1 = pd.read_sql_query(sql_1, conn);

#Print above league data frame:
df_1

#Convert Sqlite league file into csv file format:
df_1.to_csv('league.csv')

#The file will be automatically downloaded in the system

#View all data in the sqlite file:
df

#SQL query for player_attributes: 
sql_2 = """select * from player_attributes;
"""

#Read player_attributes table using pandas:
df_2 = pd.read_sql_query(sql_2,conn)

#Conert Sqlite player file into csv file format:
df_2.to_csv('player_attributes.csv')

#The file will be automatically downloaded in the sytem

#SQL query for match table:
sql_3 = """select * from Match;
"""

#Make sure connection is proper, if not, connect back to sqlite:
conn = sqlite3.connect('/Users/akankshabakshi/database.sqlite')

#Read Match table using pandas:
df_3 = pd.read_sql(sql_3, conn)

#Convert Sqlite match file to csv file format:
df_3.to_csv('match.csv')

#The file will automatically downloaded in the system

#SQL query for country table:
sql_4 = """select * from country; """

#Read country table using pandas:
df_4 = pd.read_sql_query(sql_4, conn)

#Convert Sqlite player file into csv file format:
df_4.to_csv('country.csv')

#The file will be automatically downloaded in the system

#View all data in the sqlite file:
df

#SQL query for team table:
sql_5 = """select * from team; """

#Read team table using pandas:
df_5 = pd.read_sql_query(sql_5, conn)

#Convert Sqlite team table into csv file format: 
df_5.to_csv('team.csv')

#The file will be automatically downloaded in the system

#SQL query for player table:
sql_6 = """select * from player; """

#Read player table using pandas:
df_6 = pd.read_sql_query(sql_6, conn)

#Convert Sqlite player table into csv file format:
df_6.to_csv('players.csv')

#The file will be automatically downloaded in the system

#SQL query for team_attributes:
sql_7 = """select * from team_attributes; """

#Read team_attributes using pandas:
df_7 = pd.read_sql_query(sql_7, conn)

#Convert Sqlite team_attributes file into csv file format:
df_7.to_csv('team_attributes.csv')

#The file will be automatically downloaded in the system

#Read Sqlite Sequence file
sql_8 = """select * from sqlite_sequence; """

#Read Sqlite_Sequence table using pandas: 
df_8 = pd.read_sql_query(sql_8, conn)

#Convert Sqlite Sequence table into csv file format:
df_8.to_csv('sqlite_sequence.csv')

#The file will be automatically downloaded in the system