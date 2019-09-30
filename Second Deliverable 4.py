#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

Location = "gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[ ]:


import numpy as np
df['timemgmt'] = np.where((df['exercise'] >3) & df(['hours'] > 17), 'busy', 'normal'
fr.tail(10)

