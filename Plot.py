import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel('/Users/leeli/Desktop/model/RF/pred_total.xlsx')

# plot the predicted salary VS true salary Figure
x = data['Pred']
y = data['WEEKLY_GROSS']
plt.xlabel('Pred_Salary')
plt.ylabel('True_Salary')
plt.scatter(x,y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
my_x_ticks = np.arange(-200000, 1300000, 200000)
my_y_ticks = np.arange(-200000, 1300000, 200000)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
plt.savefig('/Users/leeli/Desktop/pred_vs_true.jpg')
plt.show()