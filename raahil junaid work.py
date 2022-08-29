#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt


# In[15]:


import pandas as pd


# In[16]:


weather = pd.read_csv("https://raw.githubusercontent.com/alanjones2/dataviz/master/london2018.csv")
weather


# In[22]:


weather.plot(x="Month",y="Sun",color="yellow",marker =5,markerfacecolor="red",linestyle="--",markersize=15)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Month vs Sun")
plt.legend()
plt.show()


# In[25]:


weather.plot(x="Month",y="Rain",color="red",marker ="o",markerfacecolor="yellow",markersize=15)
plt.title("Month vs weather")
plt.show()


# In[ ]:




