#!/usr/bin/env python
# coding: utf-8

# In[301]:


import requests
import urllib.request
import time 
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns


# # Extraction of Table from Wikipedia (Medals In the oplympics)

# In[326]:


page = requests.get('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table').text
soup = BeautifulSoup(page, 'html.parser')
tables = soup.find_all('table', class_="wikitable sortable")


# In[327]:


df=pd.read_html(str(tables[0]))
Total_medals=pd.concat(df)
Total_medals.head()
Total_medals.columns=['Team','Appearances_Summer','Gold_Summer','Silver_Summer','Bronze_Summer','Total_Summer','Appearances_Winter','Gold_Winter','Silver_Winter','Bronze_Winter','Total_Winter','Appearances_Combined','Gold_Combined','Silver_Combined','Bronze_Combined','Total_Combined']
Total_medals.head()
Total_medals.head(20)
for i in range(Total_medals.shape[0]):
    Total_medals.iloc[i,0]=re.split(r'\xa0',Total_medals.iloc[i,0])[0]    


# In[328]:


df=pd.read_html(str(tables[0]))
Total_medals=pd.concat(df)
Total_medals.head()
Total_medals.columns=['Team','Appearances_Summer','Gold_Summer','Silver_Summer','Bronze_Summer','Total_Summer','Appearances_Winter','Gold_Winter','Silver_Winter','Bronze_Winter','Total_Winter','Appearances_Combined','Gold_Combined','Silver_Combined','Bronze_Combined','Total_Combined']
Total_medals.head()
Total_medals.head(20)
for i in range(Total_medals.shape[0]):
    Total_medals.iloc[i,0]=re.split(r'\xa0',Total_medals.iloc[i,0])[0]


# # Adding to the above table the average temperature and average GDP of the countries

# In[329]:


url2='https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature'
html=urllib.request.urlopen(url2)
soup=BeautifulSoup(html,'html.parser')
tables=soup.find_all('table')
df=pd.read_html(str(tables[0]))
Temp=pd.concat(df)
Temp.head()
Temp.columns=['Country','Average_Temp_Celsius']
Temp.head()
print(Temp.shape)


# In[330]:


Total_medals['Temperature']=np.zeros((157,1))
for i in range(Total_medals.shape[0]):
    t1=Temp[Temp.Country==Total_medals.loc[i,'Team']]
    if len(t1)>0:
        text=t1.Average_Temp_Celsius.values
        if len(re.findall(r"^−",text[0]))==0:
            Total_medals.loc[i,'Temperature']=t1.Average_Temp_Celsius.values
        else:
            Total_medals.loc[i,'Temperature']=re.sub(r"^−","-",text[0])
        
    else:
        Total_medals.loc[i,'Temperature']=np.nan
        
        


# In[331]:


url3='https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)#:~:text=GDP%20%28US%24%20million%29%20by%20country%20%20%20,%20%20927%20%2028%20more%20rows%20'
html=urllib.request.urlopen(url3)
soup=BeautifulSoup(html,'html.parser')
tables=soup.find_all('table')
df=pd.read_html(str(tables[2]))
GDP=pd.concat(df)
GDP=GDP.iloc[1:,:]
GDP.head()
GDP.columns
GDP_Count=pd.concat([GDP[('Country/Territory', 'Country/Territory')],GDP[(('World Bank[14][15]', 'Estimate'))]],axis=1)
GDP_Count.columns=['Country','GDP (M USD)']
Total_medals['GDP(M USD)']=np.zeros((157,1))
for i in range(Total_medals.shape[0]):
    gdp1=GDP_Count[GDP_Count.Country==Total_medals.loc[i,'Team']]
    if len(gdp1)>0:
        Total_medals.loc[i,'GDP(M USD)']=gdp1['GDP (M USD)'].values
    else:
        Total_medals.loc[i,'GDP(M USD)']=np.nan
filter11=Total_medals.Team=='Soviet Union'
Total_medals[Total_medals.Team=='Russia']


# In[332]:


Total_medals[Total_medals.Team=='Soviet Union']


# In[333]:


columns=Total_medals.columns
Total_medals['Temperature'] = pd.to_numeric(Total_medals['Temperature'],downcast='float')

filter1=Total_medals.Team=='East Germany'
filter2=Total_medals.Team=='West Germany'
for i in columns[1:-2]:
    a1=Total_medals[filter1][i].values
    a2=Total_medals[filter2][i].values
    Total_medals.loc[46,i]=Total_medals.loc[46,i]+a1[0]+a2[0]
    print(i)
filter11=Total_medals.Team=='Soviet Union'
for i in columns[1:-2]:
    a11=Total_medals[filter11][i].values    
    Total_medals.loc[108,i]=Total_medals.loc[108,i]+a11[0]
    print(i)
filter_puerto=Total_medals.Team=='Puerto Rico'
Total_medals[filter_puerto]['Temperature']=26
    #Total_medals.iloc[]+Total_medals[Total_medals.Team=='West Germany']
#Total_medals[Total_medals['Temperature'].isnull()]


# In[334]:


Total_medals[Total_medals.Team=='Russia']


# In[335]:


Total_medals.dropna(axis=0,how='any',inplace=True)


# In[336]:


first_ten_summer=Total_medals.sort_values(['Gold_Summer'],ascending=False).iloc[0:10,:]
first_ten_winter=Total_medals.sort_values(['Gold_Winter'],ascending=False).iloc[0:10,:]

fix,axes=plt.subplots(2,1,figsize=(12,7))
sns.barplot(x='Team',y='Gold_Summer',data=first_ten_summer,ax=axes[0])
sns.barplot(x='Team',y='Gold_Winter',data=first_ten_winter,ax=axes[1])

first_ten_total_summer=Total_medals.sort_values(['Total_Summer'],ascending=False).iloc[0:10,:]
first_ten_total_winter=Total_medals.sort_values(['Total_Winter'],ascending=False).iloc[0:10,:]

fix,axes=plt.subplots(2,1,figsize=(12,7))
sns.barplot(x='Team',y='Total_Summer',data=first_ten_total_summer,ax=axes[0])
sns.barplot(x='Team',y='Total_Winter',data=first_ten_total_winter,ax=axes[1])


# In[325]:


Total_medals[Total_medals.Team=='Russia']


# In[338]:


plt.figure(figsize=(8,6))
sns.regplot(x='GDP(M USD)',y='Total_Winter',data=Total_medals)
plt.figure(figsize=(8,6))
sns.regplot(x='GDP(M USD)',y='Total_Summer',data=Total_medals)


# In[339]:


print(Total_medals.loc[:,['Total_Summer','Total_Winter','Temperature']].corr())
sns.heatmap(Total_medals.loc[:,['Total_Summer','Total_Winter','Temperature']].corr(), cmap="YlGnBu")


# In[342]:


plt.figure(figsize=(8,6))
sns.regplot(x='Temperature',y='Total_Winter',data=Total_medals)
plt.figure(figsize=(8,6))
sns.regplot(x='Temperature',y='Total_Summer',data=Total_medals)
print(Total_medals.loc[:,['Total_Summer','Total_Winter','GDP(M USD)']].corr())
plt.figure(figsize=(8,6))

sns.heatmap(Total_medals.loc[:,['Total_Summer','Total_Winter','GDP(M USD)']].corr(), cmap="YlGnBu")


# In[285]:


from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

X=Total_medals.iloc[:,1:].values
X_f=StandardScaler().fit_transform(X)

wcss=[]

for i in range(2,20):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(X_f)
    wcss.append(kmeans.inertia_)
plt.plot(range(2,20),wcss)
plt.yticks([0,400,800,1200],fontweight='bold')
plt.xticks(range(2,20,2),fontweight='bold')
kmeans_best=KMeans(n_clusters=7,init='k-means++',random_state=42)
kmeans_best.fit(X_f)
plt.ylabel('wcss',fontsize=14,fontweight='bold')
plt.xlabel('Numer of clusters',fontsize=14,fontweight='bold')
kmeans_best.labels_


# In[291]:


from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(X_f)
PCA_VARS=pca.explained_variance_ratio_
pca3 = PCA(n_components=3)
principalComponents_3=pca3.fit_transform(X_f)
PCA_VARS3=pca3.explained_variance_ratio_
print('Explained variance with principal components:',100*np.sum(PCA_VARS3),'%')
print('Explained variance with principal components:',100*np.sum(PCA_VARS),'%')
clrs={0:'blue',1:'red',2:'black',3:'green',4:'yellow',5:'pink',6:'purple',7:'grey',8:'magenta',9:'yellowgreen',10:'cyan'}
clr=[]
for i in kmeans_best.labels_:
    clr.append(clrs[i])
plt.figure(figsize=(8,4))
plt.scatter(principalComponents[:,0],principalComponents[:,1],c=clr)
plt.ylabel('t2')
plt.xlabel('t1')
columns_pca=Total_medals.columns
loadings = pd.DataFrame(pca.components_.T, columns=['PC1', 'PC2'], index=columns_pca[1:])
loadings.head()
plt.figure(figsize=(8,4))
plt.scatter(principalComponents_3[:,0],principalComponents_3[:,2],c=clr)
plt.ylabel('t3')
plt.xlabel('t1')
columns_pca=Total_medals.columns
loadings_3 = pd.DataFrame(pca3.components_[[0,2],:].T, columns=['PC1', 'PC3'], index=columns_pca[1:])
loadings_3.head()


# In[293]:



import seaborn as sns
import matplotlib.pyplot as plt
loadings['name_columns']=loadings.index
def scatter_text(x, y, text_column, data, title, xlabel, ylabel):
    """Scatter plot with country codes on the x y coordinates
       Based on this answer: https://stackoverflow.com/a/54789170/2641825"""
    # Create the scatter plot
    p1 = sns.scatterplot(x, y, data=data, legend=False,s=500)
    # Add text besides each point
    ii=1
    for line in range(0,data.shape[0]):
        if ii%2==1:
            p1.text(data[x][line]+0.01, data[y][line], 
                 data[text_column][line], horizontalalignment='left',va='top' 
                 ,size='large', color='black', weight='semibold',fontsize=30
                   )
        else:
            p1.text(data[x][line]+0.01, data[y][line], 
                 data[text_column][line], horizontalalignment='right',va='bottom' 
                 ,size='large', color='black', weight='semibold',fontsize=30
                   )
        ii+=1

    # Set title and axis labels
    plt.title(title,fontsize=40)
    plt.xlabel(xlabel,fontsize=40)
    plt.ylabel(ylabel,fontsize=40)
    return p1


# In[295]:


loadings['name_columns']=loadings.index

plt.figure(figsize=(45,50))
scatter_text('PC1','PC2','name_columns',loadings,'Loading Plots','P1','P2')
plt.plot(np.zeros((100,)),np.linspace(-0.6,0.5,100),color='black')
plt.plot(np.linspace(-0.6,0.5,100),np.zeros((100,)),color='black')

plt.ylim([-0.6,0.5])
plt.xlim([-0.3,0.4])
plt.yticks([-0.6,-0.3,0,0.3,0.5],fontsize=40)
plt.xticks([-0.3,0,0.3],fontsize=40)

plt.show()


# In[283]:


loadings_3['name_columns']=loadings_3.index

plt.figure(figsize=(45,50))
scatter_text('PC1','PC3','name_columns',loadings_3,'Loading Plots','P1','P3')
plt.plot(np.zeros((100,)),np.linspace(-0.6,0.5,100),color='black')
plt.plot(np.linspace(-0.6,0.5,100),np.zeros((100,)),color='black')

plt.ylim([-0.6,0.5])
plt.xlim([-0.3,0.4])
plt.yticks([-0.6,-0.3,0,0.3,0.5],fontsize=40)
plt.xticks([-0.3,0,0.3],fontsize=40)

plt.show()


# In[273]:


plt.figure(figsize=(40,30))
scatter_text('PC1','PC3','name_columns',loadings,'Loading Plots','P1','P2')
plt.plot(np.zeros((100,)),np.linspace(-0.6,0.5,100),color='black')
plt.plot(np.linspace(-0.6,0.5,100),np.zeros((100,)),color='black')

plt.ylim([-0.6,0.5])
plt.xlim([-0.3,0.4])
plt.yticks([-0.6,-0.3,0,0.3,0.5],fontsize=40)
plt.xticks([-0.3,0,0.3],fontsize=40)

plt.show()


# In[297]:


PCA_VARS


# In[ ]:




