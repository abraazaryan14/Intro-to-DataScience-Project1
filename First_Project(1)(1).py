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


# In[15]:


#Use lambda funtion to apply the age_convert funtion to the entire age column
df['age'] = df['age'].apply(lambda age_object: str(age_object).split('-')[0])


# In[17]:


# Notice that the age type is still an object type. Convert it to numberic
df['age']= pd.to_numeric(df['age'],errors='coerce')


# In[53]:


#df['age']= pd.to_numeric(df['age'],errors='coerce') #


# In[18]:


df['age'].dtypes


# In[19]:


# Describe the dataframe after converting the age column to numeric one
df.describe()


# In[20]:


df.head(1)


# In[ ]:


# Drop the following columns: 'US_State','UK_Country' and'Age'


# In[ ]:


df.drop(['US_State', 'UK_Country', 'age'], axis=1)


# In[ ]:


# Group your dataframe by country and check the number people in the U.S. responded to the  survey


# In[21]:


df['Country'].value_counts()


# In[ ]:


# What is the median salary of the developer in 'United States of America',
#'United Kingdom of Great Britain and Northern Ireland',
#'Canada','Germany','India','France'?


# In[25]:


df_countries = df.loc[df['Country'].isin(['United States of America','United Kingdom of Great Britain and Northern Ireland','Canada','Germany','India', 'France'])]

df_countries.groupby('Country')['ConvertedCompYearly'].median()


# In[26]:


#Mean and Median
df_countries.groupby('Country')['ConvertedCompYearly'].agg(['median','mean'])


# In[ ]:


# How many people in the US work with Python?


# In[27]:


usa_df = df[df['Country']=='United States of America']
usa_df.shape


# In[29]:


python_users_usa = usa_df['LanguageHaveWorkedWith'].str.contains('Python').value_counts()
python_users_usa


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




