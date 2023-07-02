#!/usr/bin/env python
# coding: utf-8

# In[93]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor


# In[22]:


get_ipython().system('pip install xgboost')


# In[82]:


df=pd.read_csv(r"C:\Users\pc\Desktop\DS\Linear Reg\TeamInfo.csv")  ##VERİLERİMİZİN İLK SCRAPELENMİŞ HALİ


# In[285]:


df.head(-1)


# #                                         VERİLERİ TEMİZLEME VE DÜZENLEME

# In[286]:


## "marketValueAvg" içersinde yer alan sayısal verileri milyon cinsinden düzenledik.
    
for i in range(len(df['marketValueAvg'])):
    if df['marketValueAvg'][i][-1] == 'm':
        num = float(df['marketValueAvg'][i].replace('m',''))
        df['marketValueAvg'][i] = "{:.2f}".format(num)
    else:
        num = float(df['marketValueAvg'][i].replace('k', '')) / 1000.0
        df['marketValueAvg'][i] = "{:.3f}".format(num)



# {:.2f}".format(num) ifadesi, 'num' değişkenindeki sayıyı iki ondalık basamakta yuvarlayarak string formatına dönüştürür. Burada ':.2f' ifadesi, formatlama yönergeleridir. İki nokta arasındaki '2' ifadesi, kaç ondalık basamak kullanılacağını belirtir. 'f' ifadesi ise, formatlanacak değişkenin bir float (ondalık) değer olduğunu belirtir. Örneğin, num değişkeni 13.84 olsaydı, "é{:.2f}".format(num) ifadesi '13.84' stringini verecekti.
# 
# Yukarıdaki kod bloğunda, df['marketValueAvg'][i] ifadesi, veri çerçevesindeki marketValueAvg sütununun i'inci satırındaki veriyi ifade eder. num değişkeni, bu veriyi float (ondalık) türüne dönüştürür. Sonra "{:.2f}".format(num) ifadesi, num değişkenindeki sayıyı iki ondalık basamakta yuvarlayarak string formatına dönüştürür ve bu formatlanmış değeri, tekrar df['marketValueAvg'][i] ifadesiyle marketValueAvg sütununun i'inci satırına kaydeder.
# 
# 

# In[259]:


## "marketValueAvg" içersinde yer alan sayısal verileri milyon cinsinden düzenledik ve daha sonrasında "TeamInfo2.csv" içersinde kaydettik.

df=pd.read_csv(r"C:\Users\pc\Desktop\DS\Linear Reg\TeamInfo.csv")

    
for i in range(len(df['marketValueAvg'])):
    if df['marketValueAvg'][i][-1] == 'm':
        num = float(df['marketValueAvg'][i].replace('m',''))
        df['marketValueAvg'][i] = "{:.2f}".format(num)
    else:
        num = float(df['marketValueAvg'][i].replace('k', '')) / 1000.0
        df['marketValueAvg'][i] = "{:.3f}".format(num)

df.to_csv(r"C:\Users\pc\Desktop\DS\Linear Reg\TeamInfo2.csv",index=False)


# In[289]:


## "totalMarketValue" içersinde yer alan sayısal verileri milyon cinsinden düzenledik ve daha sonrasında "TeamInfo2.csv" içersinde kaydettik.

for i in range(len(df['totalMarketValue'])):
    if df['totalMarketValue'][i][-1] == 'm':
        num = float(df['totalMarketValue'][i].replace('m',''))
        df['totalMarketValue'][i] = "{:.2f}".format(num)

df.to_csv(r"C:\Users\pc\Desktop\DS\Linear Reg\TeamInfo2.csv"index=False)    #kaydetmek için 


# In[294]:


df = df.drop(columns=['Unnamed: 0'])  # "Unnamed: 0" sütununu sil
df.to_csv(r"C:\Users\pc\Desktop\DS\Linear Reg\TeamInfo2.csv", index=False)  # index sütununu dahil etme ve CSV dosyasına yazdır. BUNA DİKKAT ET.


# In[295]:


df


# In[299]:


# "ageAvg" sütunundaki "/" karakterlerini "." karakterleriyle değiştir. --> Verilerimizi çekip excell içersine attıgımızda "ageAvg" verilerimizi tarih gibi algılayıp "/" işareti koymuştu ve bunu düzelttik.
df["ageAvg"] = df["ageAvg"].str.replace("/", ".")
df.to_csv(r"C:\Users\pc\Desktop\DS\Linear Reg\TeamInfo2.csv", index=False)


# In[300]:


df


# In[302]:


df.dtypes


# In[303]:


# "ageAvg" sütununun veri tipini "float64" olarak değiştir.
df["ageAvg"] = df["ageAvg"].astype("float64")


# In[304]:


df.dtypes


# In[20]:


df=pd.read_csv(r"C:\Users\pc\Desktop\DS\Linear Reg\TeamInfo2.csv")
df


# In[21]:


## Sütun adlarını değiştirme RENAME
df = df.rename(columns={'name': 'TeamName','teamMatches':'matchesPlayed'})


# In[22]:


df['leagueName'].unique() ## Benzersiz olan verilerimizi inceleyip ona göre rename işlemi yapacağız.


# In[24]:


## "leagueName" kısmındaki "GB1" , "TR1" gibi lig isimlerini daha anlaşılır hale getirmek için isimlerini değiştirdik.
#df['leagueName'] = df['leagueName'].replace('GB1', 'Premier League')
#df['leagueName'] = df['leagueName'].replace('TR1', 'Super League')
#df['leagueName'] = df['leagueName'].replace('ES1', 'La Liga')
#df['leagueName'] = df['leagueName'].replace('IT1', 'Serie A')
#df['leagueName'] = df['leagueName'].replace('FR1', 'Ligue 1')
#df['leagueName'] = df['leagueName'].replace('L1', 'Bundesliga')

## Makine öğrenmesi modelimin sözel verilerden kurtulup daha iyi bir sonuç vermesi adına lig bilgilerini numeric hale getiriyorum.
df['leagueName'] = df['leagueName'].replace('GB1', 1)
df['leagueName'] = df['leagueName'].replace('ES1', 2)
df['leagueName'] = df['leagueName'].replace('IT1', 3)
df['leagueName'] = df['leagueName'].replace('L1', 4)
df['leagueName'] = df['leagueName'].replace('FR1', 5)
df['leagueName'] = df['leagueName'].replace('TR1', 6)


# In[28]:


# TeamName verisini siliyoruz çünkü makine öğrenmesi modeli oluştururken bu gereksiz bilgiye ihtiyacımız yok.
df = df.drop(columns=['TeamName'])


# In[26]:


print(df.info())


# In[31]:


df


# In[32]:


df.to_csv(r"C:\Users\pc\Desktop\DS\Linear Reg\TeamInfo3.csv", index=False)


# ##                                               MAKİNE ÖĞRENMESİ 

# In[26]:


df=pd.read_csv(r"C:\Users\pc\Desktop\DS\Linear Reg\TeamInfo4.csv")
df


# In[31]:


df = df.drop(columns=['points'])
df = df.drop(columns=['matchesPlayed'])


# In[109]:





# In[113]:


X=df.drop(['rank'],axis=1)
y=df['rank']

X_train, X_test , y_train , y_test=train_test_split(X,y, test_size=0.2)


# In[114]:


lr=LinearRegression()
lr.fit(X_train,y_train)


# In[115]:


lr.predict([[40,24.7,31,13.840,553.50,1]])


# In[90]:


x=lr.predict(X_test)[1:20]
x_rounded = list(map(round, x)) ## Rank'ların tam sayı olmasını istediğimden yuvarlıyorum.
x_rounded


# In[116]:


y_test[1:20]


# In[117]:


y_test


# In[118]:


df.iloc[226]


# In[91]:


lr.score(X_test,y_test)


# In[92]:


lr.score(X_train,y_train)


# In[120]:


y_train.value_counts()


# In[130]:


import xgboost as xgb
xgb_c=xgb.XGBClassifier(objective="multiclass:softmax",num_class=21)


# In[131]:


xgb_c.fit(X_train, y_train)


# In[ ]:




