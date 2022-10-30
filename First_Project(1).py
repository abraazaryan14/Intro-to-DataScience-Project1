#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[3]:


#Convert the dataset onto a pandas dataframe
df = pd.read_csv('survey_results_public.csv')


# In[4]:


#print the first five rows of the dataframe
df.head()


# In[6]:


#provide some insight about your data
df.describe()


# In[7]:


#set the maximum number of columns to 85
pd.options.display.max_rows = 85


# In[45]:


df.head(2)


# In[8]:


#reproduce the following
df.info()


# In[47]:


# We want to convert the age entries onto float/int by grabbing the first part
# of the sting. Hint( build a function called age_convert) 


# In[9]:


def age_convert(age_string):
    age_first_part = str(age_string).split('-')[0]
    return age_first_part


# In[10]:


age_convert('25-30')


# In[11]:


#Use lambda funtion to apply the age_convert funtion to the entire age column
df['Age'] = df['Age'].apply(lambda age_object: str(age_object).split('-')[0])


# In[ ]:


# Notice that the age type is still an object type. Convert it to numberic


# In[53]:


#df['age']= pd.to_numeric(df['age'],errors='coerce') #


# In[54]:


df['age'].dtypes


# In[55]:


# Describe the dataframe after converting the age column to numeric one


# In[56]:


df.head(1)


# In[ ]:


# Drop the following columns: 'US_State','UK_Country' and'Age'


# In[ ]:





# In[ ]:


# Group your dataframe by country and check the number people in the U.S. responded to the  survey


# In[59]:





# In[60]:





# In[ ]:


# What is the median salary of the developer in 'United States of America',
#'United Kingdom of Great Britain and Northern Ireland',
#'Canada','Germany','India','France'?


# In[61]:





# In[62]:


#Mean and Median


# In[ ]:


# How many people in the US work with Python?


# In[63]:





# In[64]:





# In[65]:





# In[66]:


#Reproduce the following


# In[67]:


#Reproduce the following plot of US developer aga in the x-axis and their
#salary in the y-axis


# In[68]:





# In[69]:


#Same thing for Zimbawe


# In[70]:


sns.barplot(x_1,y_1,palette='deep')
sns.despine(left=True)


# In[71]:



#Produce the following, which represent the first 20 NEWStuck in Zimbawe


# In[72]:



#how many people responded to the servey?


# In[73]:


# How many developers use Python Worldwide?


# In[74]:


know_python


# In[75]:


python_df = pd.concat([number_repondents,know_python ],axis=1)


# In[76]:


#Concatinate the number of people who reponded to the survey
# the one who know Python in one dataframe called python_df


# In[77]:



#Add a new feature called percentage


# In[78]:


python_df.head(5)


# In[79]:


#Rename the columns


# In[80]:


python_df.head(50)


# In[ ]:


#Surprise me with some plot off this later dataframe


# # Good Job!

# In[1]:


get_ipython().system('pwd')


# In[ ]:




