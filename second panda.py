#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[17]:


mdf=pd.read_csv('Movie-Data.csv')
mdf


# In[18]:


mdf.head(10)


# In[19]:


mdf.tail(10)


# In[20]:


mdf.info()


# In[21]:


mdf.describe()


# In[25]:


type(mdf)


# In[26]:


clist=mdf.columns
clist


# In[27]:


mdf=pd.read_csv('Movie-Data.csv',index_col='Title')
mdf


# In[28]:


mdf.isnull().sum()


# In[30]:


mdf.shape


# In[33]:


r=mdf['Revenue (Millions)']
r


# In[34]:


type(r)


# In[43]:


r.mean()


# In[38]:


r.median()


# In[40]:


r2=mdf[['Revenue (Millions)']]
r2


# In[41]:


type(r2)


# In[42]:


r2=mdf[['Revenue (Millions)','Year']]
r2


# In[ ]:




