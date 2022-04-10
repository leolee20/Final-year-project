import pandas as pd

data = pd.read_excel('.../RF_pred.xlsx')
data2 = pd.read_excel('.../mixed_effect_pred.xlsx')
data3 = pd.read_excel('.../Result_of_estimation.xlsx')

# Evaluate the estimation for RF model
def function1(a,b):
    if abs(a-b) / ((a+b)/2) > 0.2937:
        if a > b:
            return "Overestimation"
        else:
            return "Underestimation"
    else:
        return "Normal"

# Evaluate the estimation for Mixed-effect model
def function2(a,b,c):
    if a <= b:
        return "Underestimation"
    elif a >= c:
        return "Overestimation"
    else:
        return "Normal"

# calculate the symmetric Absolute Percentage Error for each predicted salary
def function3(a,b):
    error = abs(a-b) / ((a+b)/2)
    return error

# Compare the estimated result of mixed model and RF model
def function4(a,b):
    if a == b:
        return "Same"
    else:
        return "Different"

data['Result'] = data.apply(lambda x: function1(x['WEEKLY_GROSS'], x['Pred']), axis=1)
data['SAPE'] = data.apply(lambda x: function3(x['WEEKLY_GROSS'], x['Pred']), axis=1)
data['SAPE'] = data['SAPE'].apply(lambda x: format(x, '.2%'))
data2['Result'] = data2.apply(lambda x: function2(x['WEEKLY_GROSS'], x['down'], x['up']),axis=1)
data3['Match'] = data3[['Mixed_result','RF_result']].apply(lambda x: function4(x['Mixed_result'],x['RF_result']),axis=1)

data.to_excel('.../RF_pred.xlsx',index=False)
data2.to_excel('.../mixed_effect_pred.xlsx',index=False)
data3.to_excel('.../Result_of_estimation.xlsx',index=False)