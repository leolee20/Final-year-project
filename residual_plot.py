import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel('.../RF_pred.xlsx')
# data = pd.read_excel('.../mixed_effect_pred.xlsx')

print(data['WEEKLY_GROSS'].corr(data['Pred']))

data['residual'] = data[['WEEKLY_GROSS','Pred']].apply(lambda x: x['WEEKLY_GROSS'] - x['Pred'],axis=1)

x = list(range(1,len(data)+1))
y = data['residual']
plt.xlabel('Player')
plt.ylabel('residual')
plt.scatter(x,y,s=5)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.savefig('.../residual_plot.jpg')
plt.show()