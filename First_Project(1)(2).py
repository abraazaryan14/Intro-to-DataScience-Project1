#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


#Convert the dataset onto a pandas dataframe
df = pd.read_csv('survey_results_public.csv')


# In[3]:


#print the first five rows of the dataframe
df.head()


# In[4]:


#provide some insight about your data
df.describe()


# In[5]:


#set the maximum number of columns to 85
pd.options.display.max_rows = 85


# In[6]:


df.head(2)


# In[7]:


#reproduce the following
df.info()


# In[8]:


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


# In[12]:


# Notice that the age type is still an object type. Convert it to numberic
df['Age']= pd.to_numeric(df['Age'],errors='coerce')


# In[13]:


#df['age']= pd.to_numeric(df['age'],errors='coerce') #


# In[14]:


df['Age'].dtypes


# In[15]:


# Describe the dataframe after converting the age column to numeric one
df.describe()


# In[16]:


df.head(1)


# In[17]:


# Drop the following columns: 'US_State','UK_Country' and'Age'


# In[18]:


df.drop(['US_State', 'UK_Country', 'Age'], axis=1)


# In[19]:


# Group your dataframe by country and check the number people in the U.S. responded to the  survey


# In[20]:


df['Country'].value_counts()


# In[21]:


# What is the median salary of the developer in 'United States of America',
#'United Kingdom of Great Britain and Northern Ireland',
#'Canada','Germany','India','France'?


# In[22]:


df_countries = df.loc[df['Country'].isin(['United States of America','United Kingdom of Great Britain and Northern Ireland','Canada','Germany','India', 'France'])]

df_countries.groupby('Country')['ConvertedCompYearly'].median()


# In[23]:


#Mean and Median
df_countries.groupby('Country')['ConvertedCompYearly'].agg(['median','mean'])


# In[24]:


# How many people in the US work with Python?


# In[25]:


usa_df = df[df['Country']=='United States of America']
usa_df.shape


# In[26]:


python_users_usa = usa_df['LanguageHaveWorkedWith'].str.contains('Python').value_counts()
python_users_usa


# In[27]:


#Reproduce the following
median_salaries = df_countries.groupby('Country')['ConvertedCompYearly'].median()
median_salaries.plot.pie(figsize=(25, 20));


# In[28]:


#Reproduce the following plot of US developer aga in the x-axis and their
#salary in the y-axis


# In[ ]:


US_developer_AgeGroupby = df_countries.groupby('Age')['ConvertedCompYearly'].mean()
color_palette = ['red', 'orange', 'green', 'blue', 'yellow']
df.plot.bar(figsize=(15, 10), color=color_palette);


# In[ ]:


#Same thing for AUSTRIA
austria_df = df[df['Country']=='Austria']

plt.rcParams["figure.figsize"] = (10,8)
sns.barplot(x='Age',y='ConvertedCompYearly',data=austria_df,palette='deep')
sns.despine(left=True)


# In[ ]:


sns.barplot(x_1,y_1,palette='deep')
sns.despine(left=True)


# In[ ]:


#Produce the following, which represent the first 20 NEWStuck in Zimbawe
top_20_newstruck_austria = austria_df['newstruck'].head(20)
top_20_newstruck_austria


# In[ ]:


#how many people responded to the servey?
df['Country'].value_counts()


# In[ ]:


# How many developers use Python Worldwide?
know_python = df['LanguageHaveWorkedWith'].str.contains('Python', na=False).groupby(df['Country']).sum()
know_python


# In[ ]:


number_repondents = df['Country'].value_counts()


# In[ ]:


#Concatinate the number of people who reponded to the survey
# the one who know Python in one dataframe called python_df
python_df = pd.concat([number_repondents,know_python ],axis=1
python_df.head()


# In[ ]:


#Add a new feature called percentage
python_df['percentage'] = python_df['LanguageHaveWorkedWith'] / python_df['Country']
python_df


# In[ ]:


python_df.head(5)


# In[ ]:


#Rename the columns
python_df.rename(columns={'Country':'TotalRespondents', 'LanguageHaveWorkedWith':'NumbKnowsPython', 'percentage':'PercentDevKnowPython'}, inplace=True)


# In[ ]:


python_df.head(50)


# # Good Job!

# In[ ]:


get_ipython().system('pwd')


# In[ ]:


austria_df = df[df['Country']=='Austria']

plt.rcParams["figure.figsize"] = (12,10)
sns.barplot(x='Age',y='ConvertedCompYearly',data=austria_df,palette='deep')
sns.despine(left=True)


# In[ ]:





# In[ ]:




