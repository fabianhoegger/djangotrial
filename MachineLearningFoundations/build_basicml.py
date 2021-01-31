import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selecion import RandomForestClassifier,GridSearchCV

tr_features=pd.read_csv('train_features.csv')
tr_labels=pd.read_csv('train_labels.csv',header=None)
rf=RandomForestClassifier()
scores=cross_val_score(rf,tr_features,tr_labels.values.ravel(),cv=5)

def print_results(results):
    print("BEST PARAMS: {}\n".format(results.best_params_))
    means=results.cv_results_['mean_std_score']
    std=resutls.cv_results_['std_test_score']
    for mean,std,params in zip(means,stds,results.cv_results_['params']):
        print('{} (+/-{}) for {}'.format(round(mean,3),round(std*2,3),params))
#GridSearch
rf=RandomForestClassifier()
parameters={'n_estimators': [5,50,100],'max_depth':[2,10,20,None]}
cv=GridSearchCV(rf,parameters,cv=5)
cv=cv.fit(tr_features,tr_labels.values.ravel())
print_results(cv)

#Evaluate  3 models
rf1=RandomForestClassifier(n_estimators=5,max_depth=10)
rf1=rf1.fit(tr_features,tr_labels.values.ravel())
rf2=RandomForestClassifier(n_estimators=100,max_depth=10)
rf2=rf2.fit(tr_features,tr_labels.values.ravel())

rf3=RandomForestClassifier(n_estimators=100,max_depth=None)
rf3=rf3.fit(tr_features,tr_labels.values.ravel())