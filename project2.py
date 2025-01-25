#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pandas as pd -- To import Pandas library.
import pandas as pd


# In[4]:


#pd.read_csv - To import the CSV file in Jupyter notebook.
dat=pd.read_csv(r"C:\Users\ADMIN\Downloads\file.csv")


# In[5]:


dat


# In[10]:


#this is a Udemy Courses Dataset
#Here I will use this dataset to answer some question and provide much needed insight into the Udemy data set
#Qn1: What course subjects are offered by Udemy?
dat.subject.unique()


# In[21]:


# Udemy offers courses in 4 subjects: 
#1. Music instruments, 2. Business Finances 3. Graphic Designs 4. Web development

# Qn2. Which subject has the maximum number of courses.
dat.subject.value_counts()


# In[ ]:


#web development has the maximum number of courses with 1200 courses.


# In[22]:


#Qn3.Show all the courses which are Free of Cost.
dat.head(2)


# In[32]:


dat[dat.is_paid == False]


# In[33]:


#310 cuourses are offered for free.

#Qn.4Show all the courses which are Paid
dat[dat.is_paid == True]


# In[43]:


#Qn5.Which are Top Selling Courses ?

dat.sort_values('num_subscribers', ascending= False)


# In[50]:


#Qn6.Which are Least Selling Courses ?

dat.sort_values('num_subscribers')


# In[65]:


#Qn7.Show all courses of Graphic Design where the price is below 100 

dat[(dat.subject== 'Graphic Design') &(dat.price < '100')]


# In[68]:


#There are no graphic design courses below 100.
#Qn8.List out all the courses that are related to 'Python'

dat[dat.course_title.str.contains('Python')]


# In[74]:


#Qn9.What are courses that were published in the year 2015?

dat.dtypes


# In[75]:


dat.published_timestamp= pd.to_datetime(dat.published_timestamp)


# In[76]:


dat.dtypes


# In[82]:


dat['Year']= dat["published_timestamp"].dt.year


# In[83]:


dat


# In[90]:


dat[dat.Year == 2015]


# In[ ]:


len(dat[dat.Year == 2015])


# In[97]:


#Qn10.What is the Max. Number of Subscribers for Each Level of courses

dat.groupby("level") ['num_subscribers'].max()


# In[ ]:




