from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
from six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
import os

dataX = pd.read_excel("/Users/leeli/Desktop/model/RF/X_train.xlsx").values
dataY = pd.read_excel("/Users/leeli/Desktop/model/RF/Y_train.xlsx").values
dataY = np.ravel(dataY)

rf = RandomForestRegressor(max_features=None,n_estimators=200,max_depth=None,
                           min_samples_split=2,min_samples_leaf=1,
                           criterion="squared_error",random_state=2)
rf.fit(dataX,dataY)

feature_names=['Current_Age','POS','grade_value','Starts','Min','Gls','Ast','CrdY','CrdR','SoT','G_Sh','Pass_Att','Cmp_per',
                'TklW','Blocks','Int','Clr','Dribble_Att','Dribble_Succ_per','Carries','Targ','Rec_per',
               'League_num','Club_num']

dot_data = StringIO()
export_graphviz(rf.estimators_[0],out_file=dot_data,feature_names=feature_names)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf('/Users/leeli/Desktop/tree.pdf')
# Image(graph.create_png())