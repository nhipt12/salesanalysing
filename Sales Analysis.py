#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


get_ipython().system('pip install pyarrow')


# In[5]:


all_data = pd.read_feather(r"C:\Users\tunhi\Downloads\Udemy data/Sales_data.ftr")


# In[6]:


all_data.isnull().sum()


# In[7]:


all_data = all_data.dropna(how="all")


# In[8]:


all_data.isnull().sum()


# In[17]:


all_data[all_data.duplicated()]


# In[18]:


all_data = all_data.drop_duplicates()


# In[19]:


all_data.shape 


# In[20]:


all_data[all_data.duplicated()]


# In[21]:


all_data.head(2)


# In[34]:


all_data['Order Date'][0]


# In[35]:


'04/19/19 08:46'.split(' ')[0].split('/')[0]


# In[43]:


all_data['Order Date'][0].split('/')[0]


# In[44]:


def return_month(x):
    return x.split('/')[0]


# In[45]:


all_data['Month'] = all_data['Order Date'].apply(return_month)


# In[108]:


all_data['Month'].astype(int)


# In[47]:


all_data['Month'].unique()


# In[48]:


filter1 = all_data['Month'] == 'Order Date'


# In[49]:


all_data[~filter1]


# In[50]:


all_data = all_data[~filter1]


# In[51]:


all_data.shape


# In[52]:


import warnings
from warnings import filterwarnings
filterwarnings ('ignore')


# In[53]:


all_data['Month'] = all_data['Month'].astype(int)


# In[54]:


all_data.dtypes


# In[55]:


all_data['Quantity Ordered'] = all_data['Quantity Ordered'].astype(int)
all_data['Price Each'] = all_data['Price Each'].astype(float)


# In[56]:


all_data.dtypes


# In[60]:


all_data['sales'] = all_data['Quantity Ordered'] * all_data['Price Each']


# In[61]:


all_data.groupby(['Month'])['sales'].sum()


# In[62]:


ax = all_data.groupby(['Month'])['sales'].sum().plot(kind='bar')
ax.set_title("Monthly Sales Volume")
ax.set_ylabel("Sales")

plt.show()


# In[63]:


# From the chart, it can be seen that December had the biggest sales volume


# In[64]:


all_data['Purchase Address'][0].split(',')[1]


# In[65]:


all_data['city'] = all_data['Purchase Address'].str.split(',').str.get(1)


# In[66]:


all_data['city']


# In[67]:


pd.value_counts(all_data['city'])


# In[68]:


bx = pd.value_counts(all_data['city']).plot(kind='pie' , autopct = '%1.0f%%')
bx.set_title("Sales volume by city")
bx.set_ylabel("")


# In[69]:


count_df = all_data.groupby(['Product']).agg({'Quantity Ordered':'sum', 'Price Each':'mean'})


# In[70]:


count_df = count_df.reset_index()


# In[71]:


count_df


# In[72]:


products = count_df['Product'].values


# In[ ]:





# In[224]:


fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.bar(count_df['Product'] , count_df['Quantity Ordered'] , color='pink')
ax2.plot(count_df['Product'] , count_df['Price Each'] )
ax1.set_xticklabels(products , rotation = 'vertical', fontsize=9)

ax1.set_ylabel('Order Count')
ax2.set_ylabel('Average product price')


# In[74]:


all_data['Product'].value_counts()[0:5].index


# In[79]:


most_sold_product = all_data['Product'].value_counts()[0:5].index


# In[ ]:





# In[80]:


all_data['Product'].isin(most_sold_product)


# In[81]:


all_data[all_data['Product'].isin(most_sold_product)] 


# In[86]:


most_sold_product_df = all_data[all_data['Product'].isin(most_sold_product)] 


# In[87]:


most_sold_product_df.head(4)


# In[90]:


pivot = most_sold_product_df.groupby(['Month','Product']).size().unstack()


# In[91]:


pivot.plot(figsize=(8,6))


# In[100]:


all_data['Order ID']


# In[104]:


df_duplicated = all_data[all_data['Order ID'].duplicated(keep = False)]


# In[122]:


dup_products = df_duplicated.groupby(['Order ID'])['Product'].apply(lambda x : ','.join(x)).reset_index().rename(columns={'Product':'Grouped Products'})


# In[125]:


dup_products_df = df_duplicated.merge(dup_products, how='left', on='Order ID')


# In[148]:


dup_products_df


# In[149]:


no_dup_df = dup_products_df.drop_duplicates(subset=['Order ID'])


# In[150]:


no_dup_df.shape


# In[156]:


ax3 = no_dup_df['Grouped Products'].value_counts()[0:5].plot.pie()
ax3.set_ylabel("")


# In[ ]:




