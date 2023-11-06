#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r"C:\Users\USER\Downloads\train.csv")
df


# # 1. display top 5 rows of the dataset

# In[3]:


df.head()


# # 2. display the bottom 3 rows of this dataset

# In[5]:


df.tail(3)


# # 3. find the shape of our dataset

# In[6]:


df.shape


# In[7]:


print ("number of rows is",df.shape[0])
print("number of columns is",df.shape[1])


# # 4. get information about the dataset like number of rows,columns and their data type

# In[9]:


df.info()


# # 5. get overall statistics of the dataset

# In[13]:


df.describe(include='all')


# # 6.  data filtering

# In[17]:


df.columns


# # i. How many male passengers were there?

# In[20]:


sum(df['Sex']=='male')


# # ii. How many passengers survived?

# In[23]:


sum(df['Survived']==1)


# # 7. check for null values

# In[26]:


df.isnull().sum()


# In[27]:


import seaborn as sns
import matplotlib as plt


# In[28]:


sns.heatmap(df.isnull())


# # percentage of null values

# In[30]:


percent_null = df.isnull().sum() * 100 / len(df)
percent_null


# # 8. drop column

# In[32]:


df.drop('Cabin', axis=1,inplace=True)


# In[34]:


df.columns


# # 9. fill in missing vales

# # i. embarked column

# In[36]:


df['Embarked'].mode()


# In[37]:


df['Embarked'].fillna('s',inplace=True)


# In[38]:


df.isnull().sum()


# # ii. age column

# In[40]:


df['Age'].fillna(df['Age'].mean(),inplace=True)


# In[41]:


df.isnull().sum()


# # 10. data encoding

# # i. sex column

# In[44]:


df['Sex'].unique()


# In[46]:


df['gender']=df['Sex'].map({'male':1 ,'female':0})


# In[47]:


df.head()


# # 11. univariate analysis

# # i. how many people survived ,how many died ?

# In[50]:


df['Survived'].value_counts()


# # ii. how many passengers were in each class?

# In[57]:


df['Pclass'].value_counts()


# # 12.  bivariate analysis

# In[61]:


df.columns


# # i. who had a better chance o survival male or female

# In[63]:


sns.barplot(x='Sex',y='Survived',data=df)


# # ii. which passenger class had a better chance of survival

# In[65]:


sns.barplot(x='Pclass',y='Survived',data=df)


# # 13. feauture engineering

# # i. create family size column

# In[69]:


df['family_size']= df['SibSp']+ df['Parch']


# In[70]:


df.head()


# In[ ]:




