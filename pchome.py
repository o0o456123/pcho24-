import requests 
import json
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={}&page={}&sort=rnk/dc'.format('電鍋','1')
#format 商品 頁數
res2 = requests.get(url)
res2.encoding='utf-8'
jsondata2 = json.loads(res2.text)
iphonedata2 = jsondata2['prods']
price = []
for d in iphonedata2:
    price.append(d['price'])

X1 = (np.arange(0,20))
Y1 = np.array(price)

plt.bar(X1,Y1,align='center',facecolor='#9999FF',edgecolor='White')
for x,y in zip(X1,Y1):
    plt.text(x,y,'%s'%y, ha='center', va='bottom')
plt.show()