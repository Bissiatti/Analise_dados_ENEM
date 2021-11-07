import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV, KFold
from scipy.stats import randint
from sklearn.metrics import explained_variance_score, r2_score,max_error, mean_absolute_error

df = pd.read_csv("../ENEM_data_for_modeling.csv")

t = []
t = ['CO_UF_RESIDENCIA','NU_IDADE','TP_ANO_CONCLUIU','TP_SEXO',"IN_TREINEIRO","TP_LINGUA"]
t.extend(df.columns.tolist()[36:61])
t.extend(df.columns.tolist()[62:])

cols = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 23, 26, 28, 29, 30}


newCols= []
for i in cols:
    newCols.append(t[i])

y = df["NOTA_MEDIA"]
X = df[newCols]
xtrain, xtest, ytrain, ytest = train_test_split(X,y,test_size=0.3)


est = lgb.LGBMRegressor()

num_folds = 10
score = 'r2'
kfold = KFold(n_splits=num_folds, random_state=10, shuffle=True)
seed = 0
max_depth = [3,5,10,15,20,50,30,None]
min_samples_split_values = randint(32,128)
min_samples_leaf_values = randint(32,128)

param_distributions = {'extra_trees': [True, False],'boost_from_average': [True, False]}

lgbm_gridF = RandomizedSearchCV(estimator=est,
                                param_distributions=param_distributions,n_iter= 50, scoring=score, cv=kfold)  # Grid search

lgbm_bestF = lgbm_gridF.fit(xtrain, ytrain)  #Fit the model 

best_lgbm = lgbm_bestF.best_estimator_  # best estimator 

best_lgbm.booster_.save_model('modelMean.txt')


print(best_lgbm.predict(xtest))

print(r2_score(ytest,best_lgbm.predict(xtest)))

y = df["NU_NOTA_REDACAO"]
X = df[newCols]
xtrain, xtest, ytrain, ytest = train_test_split(X,y,test_size=0.3)


lgbm_gridF = RandomizedSearchCV(estimator=est,
                                param_distributions=param_distributions,n_iter= 50, scoring=score, cv=kfold)  # Grid search

lgbm_bestF = lgbm_gridF.fit(xtrain, ytrain)  #Fit the model 

best_lgbm = lgbm_bestF.best_estimator_  # best estimator 

best_lgbm.booster_.save_model('modelRedacao.txt')


print(best_lgbm.predict(xtest))

print(r2_score(ytest,best_lgbm.predict(xtest)))