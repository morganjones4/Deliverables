#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

Location = "gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[ ]:


bins = [0,80,100]
status_names = ['Fail','Pass']
df ['Status'] = pd.cut(df['Grade' ], bins , labels=Status_names)
pd.value_counts(df['Status '])

