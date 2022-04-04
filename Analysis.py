import pandas as pd

data = pd.read_excel('/Users/leeli/Desktop/model/RF/RF_est.xlsx')
data2 = pd.read_excel('/Users/leeli/Desktop/model/mixed_effect/prediction90_est.xlsx')

def function1(a,b):
    if abs(a-b) / ((a+b)/2) > 0.2937:
        if a > b:
            return "Overestimation"
        else:
            return "Underestimation"
    else:
        return "Normal"

def function2(a,b,c):
    if a <= b:
        return "Underestimation"
    elif a >= c:
        return "Overestimation"
    else:
        return "Normal"

def function3(a,b):
    error = abs(a-b) / ((a+b)/2)
    return error


data['Result'] = data.apply(lambda x: function1(x['WEEKLY_GROSS'], x['Pred']), axis=1)
data['Error_per'] = data.apply(lambda x: function3(x['WEEKLY_GROSS'], x['Pred']), axis=1)
data2['Result'] = data2.apply(lambda x: function2(x['Salary'], x['down'], x['up']),axis=1)

data.to_excel('/Users/leeli/Desktop/model/RF/RF_est.xlsx',index=False)
data2.to_excel('/Users/leeli/Desktop/model/mixed_effect/prediction90_est.xlsx',index=False)