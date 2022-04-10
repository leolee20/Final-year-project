
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV

dataX = pd.read_excel(".../X_train.xlsx").values # Selected features
dataY = pd.read_excel(".../Y_train.xlsx").values # Weekly Salary
dataY = np.ravel(dataY)

rf_model = RandomForestRegressor(n_estimators=200,random_state=2)
n_estimators = [10,50,100,200,300,400,500,800,1000]
random_state = range(1,50)
para = dict(n_estimators=n_estimators,random_state=random_state)

grid_search = GridSearchCV(rf_model,param_grid=para,scoring='r2',cv=5)
grid_search.fit(dataX, dataY)
print("Best: %f using %s" % (grid_search.best_score_,grid_search.best_params_))
#grid_scores_: give the result of evaluation in different parameters;
#best_params_: describe the best combination of parameters
#best_score_: the best score
means = grid_search.cv_results_['mean_test_score']
params = grid_search.cv_results_['params']
for mean,param in zip(means,params):
    print("%f  with:   %r" % (mean,param))