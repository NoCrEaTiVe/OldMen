#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets.samples_generator import make_blobs
import datetime as dt


# In[26]:


df = pd.read_csv(r'C:\Users\muhas\Downloads\export_dataframe.csv')


# In[39]:


df.drop('percentage', axis=1, inplace=True)


# In[40]:


df.head()


# In[42]:


df['lastpublication'] = df['lastpublication'].apply(pd.to_datetime)


# In[43]:


df.head()


# In[47]:


sd = dt.datetime(2019,7,7)
df['hist']= sd - df['lastpublication']
df['hist'].astype('timedelta64[D]')
df['hist']= round(df['hist'] / np.timedelta64(1, 'D'))
df.head()


# In[48]:


df


# In[49]:


df['target2'] = [0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0]


# In[55]:


df.head()


# In[56]:


y = df['target2']
X = df.drop(['lastpublication', 'target2'], axis=1)


# In[58]:


model = LogisticRegression()
model.fit(X, y)


# In[62]:


x_test = pd.DataFrame([[101, 497, 871, 12, 4, 1]], columns = ['posts', 'follows', 'followers', 'likes', 'comments', 'hist'])


# In[63]:





# In[64]:


score = model.predict_proba(x_test)


# In[79]:


scoreList = score.tolist()


# In[82]:


scoreList[0][1]

