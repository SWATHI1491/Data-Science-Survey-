#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library


df_surveys = pd.read_csv('D:\Certificates\SQL Jupyter Notebook\Audience interest in different data science topics\Topic_Survey_Assignment.csv',index_col=0)

print('Dataset downloaded and read into a pandas dataframe!')


# In[5]:


df_surveys.head()


# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df_surveys = pd.read_csv('D:\Certificates\SQL Jupyter Notebook\Audience interest in different data science topics\Topic_Survey_Assignment.csv', index_col=0)

# Sort data in descending order of 'Very interested'
df_surveys.sort_values(by='Very interested', ascending=False, inplace=True)

# Calculate percentage of respondents
total_respondents = 2233
df_pct = (df_surveys / total_respondents) * 100
df_pct = df_pct.round(2)

# Set plot parameters
fig = plt.figure(figsize=(20, 8))
ax = fig.add_subplot(1,1,1)
ax.set_title('Percentage of Respondents\' Interest in Data Science Areas', fontsize=16)

# Create bar chart
bar_width = 0.8
color_vi = '#5cb85c'
color_si = '#5bc0de'
color_ni = '#d9534f'
df_pct.plot(kind='bar', ax=ax, width=bar_width, color=[color_vi, color_si, color_ni], edgecolor='none')

# Set font size for labels, percentages, and legend
fontsize = 14
ax.set_xticklabels(df_pct.index, fontsize=fontsize)
ax.legend(fontsize=fontsize)

# Display percentages above bars
for i in ax.containers:
    ax.bar_label(i, label_type='edge', labels=i.datavalues.round(2), fontsize=fontsize)

# Remove left, top, and right borders
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()


# In[ ]:




