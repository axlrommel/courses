import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

qq2 = pd.read_csv('addresses.csv')
qq3 = pd.read_csv('latlons.csv')

df_add = qq2.merge(qq3,how='inner',on='address')

qq = pd.read_csv('train.csv')
qq['zip_code'] = qq['zip_code'].apply(lambda x: str(x)[:5])
qqa = qq.merge(df_add,how='inner', on='ticket_id')
columns_to_keep_train = ['agency_name', 'inspector_name', 'judgment_amount', 
    'violation_code', 'disposition','fine_amount','admin_fee','state_fee',
    'late_fee','discount_amount','clean_up_cost','zip_code','lat','lon','compliance']
temp = qqa[columns_to_keep_train]
train = temp.dropna(axis=0, how='any')

qq1 = pd.read_csv('test.csv')
qq1['zip_code'] = qq1['zip_code'].apply(lambda x: str(x)[:5])
qqb = qq1.merge(df_add,how='inner', on='ticket_id')
columns_to_keep_pred = ['agency_name', 'inspector_name', 'judgment_amount', 
    'violation_code', 'disposition','fine_amount','admin_fee','state_fee',
    'late_fee','discount_amount','clean_up_cost','zip_code','lat','lon']
predict = qqb[columns_to_keep_pred]



violation_codes = list(set(np.append(predict['violation_code'].unique(), train['violation_code'].unique())))
disposition = list(set(np.append(predict['disposition'].unique(), train['disposition'].unique())))
inspector_name = list(set(np.append(predict['inspector_name'].unique(), train['inspector_name'].unique())))
agency_name = list(set(np.append(predict['agency_name'].unique(), train['agency_name'].unique())))

violDict = {}
dispDict = {}
inspDict = {}
agencyDict = {}

for index in range(len(violation_codes)) :
    violDict[violation_codes[index]] = index

for index in range(len(disposition)) :
    dispDict[disposition[index]] = index

for index in range(len(inspector_name)) :
    inspDict[inspector_name[index]] = index

for index in range(len(agency_name)) :
    agencyDict[agency_name[index]] = index

predict['violation_code'].replace(violDict,inplace=True)
train['violation_code'].replace(violDict,inplace=True)
predict['disposition'].replace(dispDict,inplace=True)
train['disposition'].replace(dispDict,inplace=True)
predict['inspector_name'].replace(inspDict,inplace=True)
train['inspector_name'].replace(inspDict,inplace=True)
predict['agency_name'].replace(agencyDict,inplace=True)
train['agency_name'].replace(agencyDict,inplace=True)

columns_for_training = [
'disposition'
,'judgment_amount'
,'fine_amount'
# ,'violation_code'
# ,'inspector_name'
# ,'agency_name'
# ,'admin_fee'
# ,'state_fee'
# ,'late_fee'
# ,'discount_amount'
# ,'clean_up_cost'
# ,'zip_code'
,'lat'
,'lon'
]


if 'zip_code' in columns_for_training:
    train = train[train.zip_code.apply(lambda x: x.isnumeric())]
    predict = predict[predict.zip_code.apply(lambda x: x.isnumeric())]


X_train = train[columns_for_training]
y_train = train['compliance']


clf1 = LogisticRegression(random_state=0)
grid_values1 = {'C':[0.01, 0.1, 1, 10, 100], 'penalty':['l1','l2']}

clf2 = RandomForestClassifier(random_state=0)
grid_values2 = {'n_estimators':[5, 15, 45, 100]}

clf3 = GradientBoostingClassifier(random_state=0)
grid_values3 = {'n_estimators':[100,200], 'learning_rate':[0.001,0.01, 0.1,1], 'max_depth':[2,3,4]}

clf1run = GridSearchCV(clf1, cv=3,param_grid=grid_values1, scoring='roc_auc')
rr1 = clf1run.fit(X_train, y_train)
print(rr1.best_score_)
print(rr1.best_estimator_)

clf2run = GridSearchCV(clf2, cv=3,param_grid=grid_values2, scoring='roc_auc')
rr2 = clf2run.fit(X_train, y_train)
print(rr2.best_score_)
print(rr2.best_estimator_)

clf3run = GridSearchCV(clf3, cv=3,param_grid=grid_values3, scoring='roc_auc')
rr3 = clf3run.fit(X_train, y_train)
print(rr3.best_score_)
print(rr3.best_estimator_)

#best ones:
# 0.763466662673
# LogisticRegression(C=0.01, class_weight=None, dual=False, fit_intercept=True,
#           intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
#           penalty='l2', random_state=0, solver='liblinear', tol=0.0001,
#           verbose=0, warm_start=False)
# 0.746500432338
# RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
#             max_depth=None, max_features='auto', max_leaf_nodes=None,
#             min_impurity_split=1e-07, min_samples_leaf=1,
#             min_samples_split=2, min_weight_fraction_leaf=0.0,
#             n_estimators=100, n_jobs=1, oob_score=False, random_state=0,
#             verbose=0, warm_start=False)
# 0.794742186446
# GradientBoostingClassifier(criterion='friedman_mse', init=None,
#               learning_rate=0.1, loss='deviance', max_depth=3,
#               max_features=None, max_leaf_nodes=None,
#               min_impurity_split=1e-07, min_samples_leaf=1,
#               min_samples_split=2, min_weight_fraction_leaf=0.0,
#               n_estimators=200, presort='auto', random_state=0,
#               subsample=1.0, verbose=0, warm_start=False)


