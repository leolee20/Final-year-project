from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
import joblib

# Input the dataset
dataX = pd.read_excel("/Users/leeli/Desktop/model/RF/X_train.xlsx").values
dataY = pd.read_excel("/Users/leeli/Desktop/model/RF/Y_train.xlsx").values
dataY = np.ravel(dataY)

# Build the model
rf = RandomForestRegressor(max_features=None,n_estimators=200,max_depth=None,
                           min_samples_split=2,min_samples_leaf=1,
                           criterion="squared_error",random_state=2)
rf.fit(dataX,dataY)

# store the model into pkl file
joblib.dump(rf, "/Users/leeli/PycharmProjects/untitled/Final_project/RF_model.pkl")

# croass validation and r2 test
scores = cross_val_score(rf,dataX,dataY,scoring='r2',cv=5).mean()
r2 = rf.score(dataX, dataY)

# print feature importance table
feature_names=['Current_Age','POS','grade_value','Starts','Min','Gls','Ast','CrdY','CrdR','SoT','G_Sh','Pass_Att','Cmp_per',
                'TklW','Blocks','Int','Clr','Dribble_Att','Dribble_Succ_per','Carries','Targ','Rec_per',
               'League_num','Club_num']
feature_names = np.array(feature_names)
print("Feature importance："+str(rf.feature_importances_))
# Store the table
# fi = pd.DataFrame(rf.feature_importances_)
# fi.to_excel('/Users/leeli/Desktop/model/RF/feature_importances.xlsx', index=False)

# print feature importance ranking graph
sorted_idx = rf.feature_importances_.argsort()
plt.barh(feature_names[sorted_idx], rf.feature_importances_[sorted_idx])
plt.xlabel("Random Forest Feature Importance")
plt.show()

# predict the response variable for dataset
pred = rf.predict(dataX)
pred = pd.DataFrame(pred)
# pred.to_excel('/Users/leeli/Desktop/model/RF/Pred.xlsx',index=False)