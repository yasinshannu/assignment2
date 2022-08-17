#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[1]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[2]:


sal=pd.read_csv("Salaries.csv")


# In[3]:


sal


# In[ ]:





# ** Check the head of the DataFrame. **

# In[4]:


sal.head()


# ** Use the .info() method to find out how many entries there are.**

# In[5]:


sal.info()


# **What is the average BasePay ?**

# In[7]:


sal['BasePay'].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[8]:


sal['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[10]:


sal[sal["EmployeeName"]=="JOSEPH DRISCOLL"]["JobTitle"]


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[11]:


sal[sal["EmployeeName"]=="JOSEPH DRISCOLL"]["TotalPayBenefits"]


# ** What is the name of highest paid person (including benefits)?**

# In[13]:


sal[sal["TotalPayBenefits"]==sal["TotalPayBenefits"].max()]


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[15]:


sal[sal["TotalPayBenefits"]==sal["TotalPayBenefits"].min()]


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[17]:


sal.groupby("Year").mean("BasePay")


# ** How many unique job titles are there? **

# In[18]:


sal['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **

# In[25]:


g=sal.groupby("JobTitle").count()
top5=g.sort_values(by='Id',ascending=False)[:5]
top5['Id']


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[31]:


cd_sal = sal[sal['Year'] == 2013]
grp = cd_sal.groupby('JobTitle').count()
count = grp[group['Id'] == 1]
count.count()['Id']


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[32]:


def find_chief(job_title):    
    if 'chief' in job_title.lower().split():
        return True
    else:
        return False

sal = pd.read_csv('Salaries.csv')

sum(sal['JobTitle'].apply(lambda x: find_chief(x)))


# In[33]:


def find_chief(job_title):    
    if 'chief' in job_title.lower().split():
        return True
    else:
        return False

sal = pd.read_csv('Salaries.csv')

sum(sal['JobTitle'].apply(lambda x: find_chief(x)))


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[22]:





# In[34]:


sal['t-len'] = sal['JobTitle'].apply(len)

sal[['t-len', 'TotalPayBenefits']].corr()


# # Great Job!

# In[ ]:




