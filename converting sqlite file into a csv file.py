#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlite3


# In[2]:


conn = sqlite3.connect('/Users/akankshabakshi/database.sqlite')


# In[3]:


sql = "select * from sqlite_master where type = 'table';"


# In[4]:


df = pd.read_sql_query(sql, conn);


# In[5]:


df


# In[6]:


sql_1 = """select * from league;
"""


# In[7]:


df_1 = pd.read_sql_query(sql_1, conn);


# In[8]:


df_1


# In[9]:


df_1.to_csv('league.csv')


# In[61]:


df_1


# In[62]:


df


# In[28]:


#converting_player_attributes_from_sqlitefile_to_csv 
sql_2 = """select * from player_attributes;
"""


# In[29]:


#converting_player_attributes_from_sqlitefile_to_csv
df_2 = pd.read_sql_query(sql_2,conn)


# In[30]:


#converting_player_attributes_from_sqlitefile_to_csv
df_2.to_csv('player_attributes.csv')


# In[63]:


#converting_match_from_sqlitefile_to_csv
sql_3 = """select * from Match;
"""


# In[64]:


conn = sqlite3.connect('/Users/akankshabakshi/database.sqlite')


# In[68]:


df_3 = pd.read_sql(sql_3, conn)


# In[69]:


df_3.to_csv('match.csv')


# In[70]:


#converting_country_from_sqlitefile_to_csv
sql_4 = """select * from country; """


# In[71]:


#converting_country_from_sqlitefile_to_csv
df_4 = pd.read_sql_query(sql_4, conn)


# In[72]:


#converting_country_from_sqlitefile_to_csv
df_4.to_csv('country.csv')


# In[73]:


df_4


# In[74]:


#to view tables back again
df


# In[75]:


sql_5 = """select * from team; """


# In[76]:


df_5 = pd.read_sql_query(sql_5, conn)


# In[77]:


df_5


# In[78]:


#converting team sqlite file into csv 
df_5.to_csv('team.csv')


# In[80]:


df


# In[81]:


sql_6 = """select * from player; """


# In[83]:


df_6 = pd.read_sql_query(sql_6, conn)


# In[84]:


df_6.head()


# In[85]:


#converting players sqlite file into csv file
df_6.to_csv('players.csv')


# In[86]:


df


# In[87]:


sql_7 = """select * from team_attributes; """


# In[88]:


df_7 = pd.read_sql_query(sql_7, conn)


# In[90]:


#converting player attreibutes sqlite file into csv format
df_7.to_csv('team_attributes.csv')


# In[91]:


sql_8 = """select * from sqlite_sequence; """


# In[92]:


df_8 = pd.read_sql_query(sql_8, conn)


# In[93]:


df_8


# In[95]:


df_8.to_csv('sqlite_sequence.csv')


# In[ ]:




