#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis - Terrorism

# ## Author: Muskan Jain

# Dataset: https://bit.ly/2TK5Xn5

# # Importing Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings("ignore")


# # Observing Dataset

# In[2]:


df=pd.read_csv("C:\\Users\\91741\\Downloads\\Base for Analysis.csv",encoding="latin-1")
df.head()


# In[3]:


df.info()


# In[4]:


df.shape


# In[5]:


df.columns


# # Data Preprocessing

# ## Important Columns 

# In[6]:


df=df[["iyear","imonth","iday","country_txt","region_txt","city",
       "latitude","longitude","attacktype1_txt","targtype1_txt",
       "gname","weaptype1_txt","nkill","nwound"]]
df.head()


# In[7]:


df.rename(columns={"iyear":"Year","imonth":"Month","iday":"Day","country_txt":"Country",
                   "region_txt":"Region","city":"City",
                   "latitude":"Latitude","longitude":"Longitude",
                  "attacktype1_txt":"Attack Type","targtype1_txt":"Target Type",
                   "gname":"Group Name","weaptype1_txt":"Weapon Type",
                   "nkill":"Killed","nwound":"Wounded"},inplace=True)


# In[8]:


df.head()


# In[9]:


df.info()


# In[10]:


df.shape


# In[11]:


df.isnull().sum()


# # Handling Missing values

# In[12]:


df["Killed"]=df["Killed"].fillna(0)
df["Wounded"]=df["Wounded"].fillna(0)


# In[13]:


df.describe()


# ## Visualizing the data

# ### 1. Year wise Attacks

# In[14]:


attacks=df["Year"].value_counts(dropna=False).sort_index().to_frame().reset_index().rename(columns={"index":"Year","Year":"Attacks"}).set_index("Year")
attacks.head()


# In[15]:


attacks.plot(kind="bar",figsize=(15,6),fontsize=13)
plt.title("Timeline of Attacks",fontsize=15)
plt.xlabel("Years",fontsize=15)
plt.ylabel("Number of Attacks",fontsize=15)
plt.show()


# ## Most number of attacks happened in 2014

# ## 2. Killed per year

# In[16]:


yk=df[["Year","Killed"]].groupby("Year").sum()
yk.head()


# In[17]:


fig=plt.figure()
ax0=fig.add_subplot(2,1,1)

#Killed
yk.plot(kind="bar",figsize=(15,15),ax=ax0)
ax0.set_title("People Killed in each Year")
ax0.set_xlabel("Years")
ax0.set_ylabel("Number of People Killed") 


# ###  Most people killed in 2014

# # 3. Wounded per year

# In[18]:


yw=df[["Year","Wounded"]].groupby("Year").sum()
yw.head()


# In[19]:


fig=plt.figure()
ax1=fig.add_subplot(2,1,2)

#Wounded
yw.plot(kind="bar",figsize=(15,15),ax=ax1)
ax1.set_title("People Wounded in each Year")
ax1.set_xlabel("Years")
ax1.set_ylabel("Number of People Wounded")

plt.show()


# ###  Most people wounded in 2014

# # 2. Region wise Attacks

# In[25]:


region=pd.crosstab(df.Year,df.Region)
region.head()


# In[26]:


region.plot(kind='area',figsize=(20,10))
plt.title("Region wise attacks",fontsize=20)
plt.xlabel("Years",fontsize=20)
plt.ylabel("Number of Attacks",fontsize=20)
plt.show()


# In[23]:


regt=region.transpose()
regt["Total"]=regt.sum(axis=1)
ra=regt["Total"].sort_values(ascending=False)
ra


# In[24]:


ra.plot(kind="bar",figsize=(15,6))
plt.title("Total Number of Attacks in each Region from 1970-2017")
plt.xlabel("Region")
plt.ylabel("Number of Attacks")
plt.show()


# ### Most attacks  occurred in Middle East and North Africa

# # 4. Killed in each Region

# In[27]:


rk=df[["Region","Killed"]].groupby("Region").sum().sort_values(by="Killed",ascending=False)
rk


# In[30]:


fig=plt.figure()
ax0=fig.add_subplot(1,2,1)

#Killed
rk.plot(kind="bar",figsize=(15,6),ax=ax0)
ax0.set_title("People Killed in each Region")
ax0.set_xlabel("Regions")
ax0.set_ylabel("Number of People Killed")


# ### Most people were killed in Middle East and North Africa

# # 5. Wounded in each Region

# In[34]:


rw=df[["Region","Wounded"]].groupby("Region").sum().sort_values(by="Wounded",ascending=False)
rw


# In[93]:


fig=plt.figure()

ax1=fig.add_subplot(1,2,2)

#Wounded
rw.plot(kind="bar",figsize=(15,6),ax=ax1)
ax1.set_title("People Wounded in each Region")
ax1.set_xlabel("Regions")
ax1.set_ylabel("Number of People Wounded")

plt.show()


# # 3. Country wise Attacks 

# In[37]:


ct=df["Country"].value_counts().head(10)
ct


# In[38]:


ct.plot(kind="bar",figsize=(15,6))
plt.title("Country wise Attacks",fontsize=13)
plt.xlabel("Countries",fontsize=13)
plt.xticks(fontsize=12)
plt.ylabel("Number of Attacks",fontsize=13)
plt.show()


# ### Most attacks happened in Iraq

# # Country wise killed 

# In[39]:


count_k=df[["Country","Killed"]].groupby("Country").sum().sort_values(by="Killed",ascending=False)
count_k.head(10)


# In[41]:


fig=plt.figure()
ax0=fig.add_subplot(1,2,1)

#Killed
count_k[:10].plot(kind="bar",figsize=(15,6),ax=ax0)
ax0.set_title("People Killed in each Country")
ax0.set_xlabel("Countries")
ax0.set_ylabel("Number of People Killed")


# ### Mostly people were killed in Iraq

# # Country wise wounded

# In[42]:


country_w=df[["Country","Wounded"]].groupby("Country").sum().sort_values(by="Wounded",ascending=False)
country_w.head(10)


# In[94]:


fig=plt.figure()
ax1=fig.add_subplot(1,2,2)
#Wounded
country_w[:10].plot(kind="bar",figsize=(15,6),ax=ax1)
ax1.set_title("People Wounded in each Country")
ax1.set_xlabel("Countries")
ax1.set_ylabel("Number of People Wounded")

plt.show()


# ### Most people were wounded in Iraq

# # 4. City wise Attacks 

# In[50]:


city=df["City"].value_counts()[1:11]
city


# In[56]:


city.plot(kind="bar",figsize=(15,6))
plt.title("City wise Attacks",fontsize=13)
plt.xlabel("Cities",fontsize=13)
plt.xticks(fontsize=12)
plt.ylabel("Number of Attacks",fontsize=13)
plt.show()


# ### Most attacks happened in Baghdad

# # City Wise Killed

# In[58]:


city_k=df[["City","Killed"]].groupby("City").sum().sort_values(by="Killed",ascending=False).drop("Unknown")
city_k.head(10)


# In[61]:


fig=plt.figure()
ax0=fig.add_subplot(1,2,1)
#Killed
city_k[:10].plot(kind="bar",figsize=(15,6),ax=ax0)
ax0.set_title("People Killed in each City")
ax0.set_xlabel("Cities")
ax0.set_ylabel("Number of People Killed")


# ### Most people were killed in Baghdad

# # City Wise Wounded

# In[62]:


city_w=df[["City","Wounded"]].groupby("City").sum().sort_values(by="Wounded",ascending=False).drop("Unknown")
city_w.head(10)


# In[64]:


fig=plt.figure()
ax1=fig.add_subplot(1,2,2)

#Wounded
city_w[:10].plot(kind="bar",figsize=(15,6),ax=ax1)
ax1.set_title("People Wounded in each City")
ax1.set_xlabel("Cities")
ax1.set_ylabel("Number of People Wounded")

plt.show()


# ### Most people were wounded in Baghdad

# # 5. Terrorist Group wise Attacks

# In[65]:


group=df["Group Name"].value_counts()[1:10]
group


# In[66]:


group.plot(kind="bar",figsize=(15,6))
plt.title("Group wise Attacks",fontsize=13)
plt.xlabel("Terrorist Groups",fontsize=13)
plt.xticks(fontsize=12)
plt.ylabel("Number of Attacks",fontsize=13)
plt.show()


# ### Taliban has caused most number of attacks

# # Group wise Killing

# In[67]:


group_k=df[["Group Name","Killed"]].groupby("Group Name").sum().sort_values(by="Killed",ascending=False).drop("Unknown")
group_k.head(10)


# In[70]:


fig=plt.figure()
ax0=fig.add_subplot(1,2,1)

#Killed
group_k[:10].plot(kind="bar",figsize=(15,6),ax=ax0)
ax0.set_title("People Killed by each Group")
ax0.set_xlabel("Terrorist Groups")
ax0.set_ylabel("Number of people Killed")


# ### Taliban caused major killing 

# # Group wise wounded

# In[69]:


group_w=df[["Group Name","Wounded"]].groupby("Group Name").sum().sort_values(by="Wounded",ascending=False).drop("Unknown")
group_w.head(10)


# In[73]:


fig=plt.figure()
ax1=fig.add_subplot(1,2,2)
#Wounded
group_w[:10].plot(kind="bar",figsize=(15,6),ax=ax1)
ax1.set_title("People Wounded by each Group")
ax1.set_xlabel("Terrorist Groups")
ax1.set_ylabel("Number of people Wounded")
plt.show()


# ### Taliban group wounded major people

# # Attacks from different Attack type

# In[74]:


weopen_at=df["Attack Type"].value_counts()
weopen_at


# In[76]:


weopen_at.plot(kind="bar",figsize=(15,6))
plt.title("Types of Attacks",fontsize=13)
plt.xlabel("Attack Types",fontsize=13)
plt.xticks(fontsize=12)
plt.ylabel("Number of Attacks",fontsize=13)
plt.show()


# ### Bombing And Explosion resulted in major attacks

# #  People Killed by different attacks

# In[83]:


weopen_k=df[["Attack Type","Killed"]].groupby("Attack Type").sum().sort_values(by="Killed",ascending=False)
weopen_k


# In[79]:


fig=plt.figure()
ax0=fig.add_subplot(1,2,1)

#Killed
weopen_k.plot(kind="bar",figsize=(15,6),ax=ax0)
ax0.set_title("People Killed in each Attack Type")
ax0.set_xlabel("Attack Types")
ax0.set_ylabel("Number of people Killed")


# ### Most people were killed by Armed Assault Attack

# # People wounded by different attacks

# In[80]:


weopen_w=df[["Attack Type","Wounded"]].groupby("Attack Type").sum().sort_values(by="Wounded",ascending=False)
weopen_w


# In[82]:


fig=plt.figure()
ax1=fig.add_subplot(1,2,2)

#Wounded
weopen_w.plot(kind="bar",figsize=(15,6),ax=ax1)
ax1.set_title("People Wounded in each Attack Type")
ax1.set_xlabel("Attack Types")
ax1.set_ylabel("Number of people Wounded")
plt.show()


# ### Most people were wounded by Bombing/Explosion activities

# ### 7. Target Type wise Attacks

# In[84]:


target_a=df["Target Type"].value_counts()
target_a


# In[85]:


target_a.plot(kind="bar",figsize=(15,6))
plt.title("Types of Targets",fontsize=13)
plt.xlabel("Target Types",fontsize=13)
plt.xticks(fontsize=12)
plt.ylabel("Number of Attacks",fontsize=13)
plt.show()


# ### Private Citizens And Property were the main targets

# # Target Group Killing

# In[87]:


target_k=df[["Target Type","Killed"]].groupby("Target Type").sum().sort_values(by="Killed",ascending=False)
target_k


# In[88]:


fig=plt.figure()
ax0=fig.add_subplot(1,2,1)

#Killed
target_k.plot(kind="bar",figsize=(17,6),ax=ax0)
ax0.set_title("People Killed in each Target Attack")
ax0.set_xlabel("Target Types")
ax0.set_ylabel("Number of people Killed")


# ### People belonging to Private Citizens and Property were killed majorly

# # Target Group Wounded

# In[89]:


target_w=df[["Target Type","Wounded"]].groupby("Target Type").sum().sort_values(by="Wounded",ascending=False)
target_w


# In[90]:


fig=plt.figure()
ax1=fig.add_subplot(1,2,2)
#Wounded
target_w.plot(kind="bar",figsize=(17,6),ax=ax1)
ax1.set_title("People Wounded in each Target Attack")
ax1.set_xlabel("Target Types")
ax1.set_ylabel("Number of people Wounded")
plt.show()


# ### People related to Private Citizens and Property were wounded majorly

# # Observations and Conclusions

# **After performing the Exploratory Data Analysis we get the following insights from the data:**
# 
# Large number of attacks happened in 2014
# 
# Private Citizens and Property were the major target for the terrorist activities
# 
# Most of the people were wounded and killed in Middle East Asia and North Africa
# 
# Iraq was the country which was most affected by terror attacks and had maximum number of killed and wounded people.
# 
# The State and City that was most affected was Baghdad
# 
# The most common attack type was Bombing/Explosion
# 
# Taliban is a major terrorist group
# 
# **Recommendation**
# 
# More surveillance is required especially in the Middle East & North African Regions.
# 
# Since Private Citizens and Property are being targeted consistently so stronger security should be provided, especially in the dense populated regions.
# 
# Strict border policy should be implemented to prevent the movement of explosives between the regions.

# In[ ]:




