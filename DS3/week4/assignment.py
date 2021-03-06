import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier

qq2 = pd.read_csv('addresses.csv')
qq3 = pd.read_csv('latlons.csv')
qq3['lat'] = qq3['lat'].fillna(42.390126).astype(float)
qq3['lon'] = qq3['lon'].fillna(-89.930867).astype(float)

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
columns_to_keep_pred = ['ticket_id','agency_name', 'inspector_name', 'judgment_amount', 
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

columns_for_test = columns_for_training[:]
columns_for_test.append('ticket_id')
X_test = predict[columns_for_test]
X_test = X_test.set_index(['ticket_id'])

X_train = train[columns_for_training]
y_train = train['compliance']


clf = GradientBoostingClassifier(criterion='friedman_mse', init=None,
              learning_rate=0.1, loss='deviance', max_depth=3,
              max_features=None, max_leaf_nodes=None,
              min_samples_leaf=1,
              min_samples_split=2, min_weight_fraction_leaf=0.0,
              n_estimators=200, presort='auto', random_state=0,
              subsample=1.0, verbose=0, warm_start=False)

results = pd.Series()
clf.fit(X_train, y_train)
for index, row in X_test.iterrows():
    pr = clf.predict_proba([row])[:, 1]
    results.set_value(index,pr[0])

print (results.describe())