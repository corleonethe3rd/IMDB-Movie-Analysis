#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


#importing csv files and rename the header
df = pd.read_csv(r"C:\Users\solop\OneDrive\Documents\Python Project IMDB movies dataset.csv",header = None, names =['Names','Date','Rating','Genre','Overview','Crew','Title','Status','Language','Budget','Revenue','Country'])


# In[117]:


df


# In[6]:


#Dsiplay every single row 
pd.set_option('display.max.rows', 10180)


# In[7]:


#Display information about the data set
df.info()


# In[8]:


#find any missing value
print ("missing values",df.isnull().values.any())


# In[9]:


df.isnull()


# In[10]:


df.isnull() .sum()


# In[10]:


sns.heatmap(df.isnull())


# In[116]:


df.dropna(axis=0)


# In[12]:


df = df.drop(0)


# In[115]:


df


# In[14]:


#check for duplicates and format the values to 2sf
df.duplicated().any()
pd.set_option('display.float_format',lambda x:'%.2f' %x)


# In[16]:


selected_columns = ['Rating', 'Budget', 'Revenue']
selected_summary_stats = df[selected_columns].describe()
print(selected_summary_stats)


# In[17]:


#converting from object to float
columns_to_convert =  ['Rating', 'Budget', 'Revenue']
df[columns_to_convert] = df[columns_to_convert].astype(float)
print(df.dtypes)


# In[18]:


#changing the date column to date time format
df['Date'] = pd.to_datetime(df['Date'])


# In[114]:


df


# In[20]:


df.columns


# In[113]:


#Investigate revenues generated across years for IMDB movies.
df.groupby(df['Date'].dt.year)[ 'Revenue'].mean().sort_values(ascending = False)


# In[34]:


df['Decade'] = (df['Date'].dt.year // 10) * 10
revenues_by_decade = df.groupby('Decade')['Revenue'].sum()


# In[112]:


revenues_by_decade


# In[40]:


#Visualization graph for total revenues of imdb movies by decade
plt.figure(figsize=(10, 6))
revenues_by_decade.plot(kind='line', color='red')
plt.title('Total Revenues of IMDb Movies by Decade')
plt.xlabel('Decade')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.show()


# In[43]:


#Relationship between revenue and budget
sns.scatterplot(x='Budget', y='Revenue', data=df)


# In[44]:


df.columns


# In[66]:


#Which country generated the highest revenue in movies
total_revenue_by_country = df.groupby('Country')['Revenue'].sum()
highest_revenue_country = total_revenue_by_country.idxmax()
print(f"The country with the highest movie revenue is: {highest_revenue_country}")


# In[110]:


#Top 15 countries with the highest revenue
total_revenue_by_country_sorted = total_revenue_by_country.sort_values(by='Revenue', ascending=False).head(15)

total_revenue_by_country_sorted


# In[106]:


#Visualization for Which country generated the highest revenue in movies
plt.figure(figsize=(12, 6))
sns.barplot(x='Country', y='Revenue', data=total_revenue_by_country_sorted)
plt.title("Total Revenue by Country")
plt.xlabel("Country")
plt.ylabel("Total Revenue")
plt.show()


# In[120]:


df.columns


# In[138]:


#the highest rated movie and which genre does it belong to
df[df['Rating'].max()==df['Rating']][['Title', 'Genre','Rating']]


# In[139]:


#Does movie budget affect movie rating? Show this with your analysis
correlation_coefficient = df['Budget'].corr(df['Rating'])


# In[140]:


correlation_coefficient


# In[141]:


plt.figure(figsize=(8, 6))
sns.scatterplot(x='Budget', y='Rating', data=df)
plt.title(f'Scatter Plot: Budget vs Rating\nCorrelation Coefficient: {correlation_coefficient:.2f}')
plt.xlabel('Budget')
plt.ylabel('Rating')
plt.show()


# In[ ]:




