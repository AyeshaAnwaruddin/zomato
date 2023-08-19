#!/usr/bin/env python
# coding: utf-8

# In[85]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use("dark_background")

get_ipython().run_line_magic('matplotlib', 'inline')
import warnings 
warnings.filterwarnings("ignore")


# In[11]:


df=pd.read_csv('zomato.csv')


# In[12]:


df.head()


# In[13]:


df.columns


# In[14]:


df.columns.value_counts()


# In[16]:


df.describe()


# In[18]:


df.isnull().sum()


# In[19]:


df.dropna()


# In[20]:


df.isna().sum()


# In[22]:


df.dropna(inplace=True)


# In[23]:


df.isnull().sum()


# In[24]:


df.shape


# In[26]:


df.duplicated().sum()


# In[29]:


df['name'].value_counts()


# In[31]:


df['rest_type'].value_counts()


# In[33]:


rest_type=df['rest_type'].value_counts()


# In[34]:


rest_type_less_1000=rest_type[rest_type<1000]


# In[35]:


rest_type_less_1000


# In[36]:


def rest_type(data):
    if data in rest_type_less_1000:
        return "other"
    else:
        return data


# In[37]:


df["rest_type"]=df["rest_type"].apply(rest_type)


# In[38]:


df['rest_type'].value_counts()


# In[39]:


df["location"].value_counts()


# In[40]:


location=df['location'].value_counts(ascending=True)
location 


# In[41]:


location_less=location[location<1000]
location_less


# In[42]:


def loactions(data):
    if data in location_less:
        return "other locations"
    else:
        return data
    


# In[45]:


df['location']=df['location'].apply(loactions)


# In[46]:


df['location'].value_counts()


# In[48]:


df['cuisines'].value_counts()


# In[49]:


cuisines=df['cuisines'].value_counts()
cuisines


# In[50]:


cuisines_less=cuisines[cuisines<250]
cuisines_less


# In[51]:


def food(data):
    if data in cuisines_less:
        return "Other Cuisines"
    else:
        return data


# In[52]:


df['cuisines']=df['cuisines'].apply(food)


# In[54]:


df['cuisines'].value_counts()


# In[57]:


#rename of columns

df.rename(columns={'approx_cost(for two people)':'Costfor2','listed_in(type)':'type'},inplace=True)


# In[58]:


df.columns


# In[59]:


df['type'].value_counts()


# In[62]:


#cleaning the rating column

df["rate"].unique()


# In[69]:


def rate(data):
    if  data=="-" or data=="NEW":
        return np.nan
    else:
        data=str(data).split('/')
        data=data[0]
        return float(data)


# In[70]:


df['rate']=df['rate'].apply(rate)


# In[71]:


df["rate"].unique()


# In[72]:


df['rate'].mode()


# In[73]:


df['rate']=df['rate'].fillna(df['rate'].mode()[0])


# In[74]:


df["rate"].unique()


# In[81]:


df.drop(['address','dish_liked','menu_item'],axis=1 ,inplace=True)


# In[82]:


df.columns


# In[92]:


# Let's Analyse location vs number of restarant 

plt.figure(figsize=(16,5))
ax = sns.countplot(x='location',data=df)
plt.xticks(rotation=90)
plt.show()
           


# In[93]:


sns.countplot(x='book_table', data=df)


# In[94]:


sns.countplot(x='online_order', data=df)


# In[95]:


#online order and rating given by the customer

sns.boxplot(data=df,x='online_order',y='rate')


# In[96]:


#book table and rating given by the customer

sns.boxplot(data=df,x='book_table',y='rate')


# In[97]:


df1=df.groupby(['location','online_order'])['name'].count()


# In[98]:


df1


# In[ ]:




