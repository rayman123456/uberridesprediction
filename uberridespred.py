#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import pickle


# In[2]:


dataset=pd.read_csv('taxi.csv')
dataset.head()


# In[3]:


dataset.isnull().sum()


# In[5]:


X=dataset.iloc[:,0:4].values
y=dataset.iloc[:,4].values


# In[6]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)


# In[8]:


from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X_train,y_train)


# In[9]:


print("Train score:",reg.score(X_train,y_train))
print("Test score:",reg.score(X_test,y_test))


# In[10]:


pickle.dump(reg,open('taxi.pkl','wb'))


# In[11]:


model=pickle.load(open('taxi.pkl','rb'))


# In[12]:


pred=model.predict([[80,1770000,6000,85]])[0].round(2)
pred


# In[ ]:




