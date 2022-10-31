#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


df = pd.read_csv('survey_results_public.csv')


# In[3]:


def age_convert(age_string):
    age_first_part = str(age_string).split('-')[0]
    return age_first_part


# In[4]:


df['Age'] = df['Age'].apply(lambda age_object: str(age_object).split('-')[0])


# In[5]:


df['Age']= pd.to_numeric(df['Age'],errors='coerce')


# In[6]:


pd.set_option("display.max_rows", None)


# In[7]:


df['Country'].value_counts()


# In[8]:


df_countries = df.loc[df['Country'].isin(['United States of America','United Kingdom of Great Britain and Northern Ireland','Canada','Germany','India', 'France'])]

df_countries.groupby('Country')['ConvertedCompYearly'].median()


# In[9]:


df_countries.groupby('Country')['ConvertedCompYearly'].agg(['median','mean'])


# In[10]:


print('Hello World')


# In[11]:


Austria_df = df[df['Country']=='Austria']
Austria_df.shape


# In[29]:


df['Gender']= pd.to_numeric(df['Gender'],errors='coerce')


# In[30]:


Gender_Users_Austria = Austria_df['Gender'].str.contains('Man' and 'Woman').value_counts()[True]
Gender_Users_Austria


# In[31]:


df['Gender'].dtypes


# In[32]:


df['Age'].dtypes


# In[37]:


df['Trans'].dtypes


# In[38]:


df['Trans'] = df['Trans'].astype(str)


# In[40]:


plt.rcParams["figure.figsize"] = (20,15)

sns.barplot(x = 'Trans', y = 'ConvertedCompYearly', data = Austria_df)
sns.despine(left=True)


# In[13]:


median_salaries = df_countries.groupby('Country')['ConvertedCompYearly'].median()


# In[14]:


converted_comp_austria = df.loc[df['Country'].isin(['Austria'])]
converted_austria = converted_comp_austria.median()


# In[ ]:


df['']= pd.to_numeric(df['Age'],errors='coerce')


# In[21]:


df['Gender'].dtypes

