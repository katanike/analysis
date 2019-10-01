# python 3 


############################## 
# model for ensemble training #
#                             #
##############################

# analytics 
import pandas as pd, numpy as np

# ml 
from sklearn import preprocessing
from sklearn import cluster, tree, decomposition
from sklearn.cross_validation import train_test_split
from sklearn.externals.six import StringIO
from sklearn.metrics import silhouette_score
from sklearn import svm
from sklearn.svm import SVC
from sklearn import neighbors, linear_model, svm, tree, ensemble

# self defined scripts 
from utility_data_preprocess import *
from utility_ML import * 



# ML 

def train():

    df = load_data()
    df_ = data_preprocess(df)
    df_ = order_value_feature(df_)
    df_ = time_feature(df_)
    df_ = label_feature(df_)
    df_train = finalize_user_profile(df_)
    df_train = data_clean(df_train)

    # get train set 
    X = df_train.iloc[:,1:].fillna(0)
    X_std = X.copy()
    # standardize 
    for i in X:
        X_std[i] = preprocessing.scale(X_std[i])
    # kmeans 
    # fix random_state here for same results (in dev)(same starting point)
    ### but will make random_state = None (in product), since random intitial state can always give better results 
    cluster_set = range(5,6)
    for cluser_ in cluster_set:
        kmean = cluster.KMeans(n_clusters=cluser_, max_iter=300, random_state=4000)
        kmean.fit(X_std)
        X_std['group'] = kmean.labels_
        df_train['group'] = kmean.labels_
        #print (X_std)
        #############

        # print classify results as table 
        group_outcome = df_train.groupby('group').mean()  
        group_user_count =  df_train.groupby('group').count()['customer_id'].reset_index().set_index('group')
        group_user_count.columns = ['group_user_count']
        group_outcome_ = group_outcome.join(group_user_count, how='inner')
        print (group_outcome_.iloc[:,1:])
    return df_train, df_ 




if __name__ == '__main__':
	######  get data ###### 
    svc_columns = [ 'order_count',
                    'sum_original_value',
                    'sum_discount_value', 
                    'sum_spend_value',
                    'avg_original_value',
                    'avg_discount_value', 
                    'avg_spend_value', 
                    'using_period', 
                    'user_period',
                    'period_no_use', 
                    'platform_']

    df_train, df_  = train()
    df_train_ = df_train.dropna()
    xtrain = df_train_[svc_columns]
    ytrain = df_train_['group']
    X_train, X_valid, y_train, y_valid = train_test_split(xtrain, ytrain,train_size=0.8, test_size=0.2)
    ###### ML  ###### 
    print ('SVM classify')
    print ('----------------')
    svc = Class_Fit(clf = svm.LinearSVC)
    svc.grid_search(parameters = [{'C':np.logspace(-2,2,10)}], Kfold = 5)
    svc.grid_fit(X =X_train, Y = y_train)
    svc.grid_predict(X_valid, y_valid)
    print ('----------------')
    print ('KNN')
    knn = Class_Fit(clf = neighbors.KNeighborsClassifier)
    knn.grid_search(parameters = [{'n_neighbors': np.arange(1,50,1)}], Kfold = 5)
    knn.grid_fit(X = X_train, Y = y_train)
    knn.grid_predict(X_valid, y_valid)
    print ('----------------')
    print (' RF random forest ')
    rf = Class_Fit(clf = ensemble.RandomForestClassifier)
    param_grid = {'criterion' : ['entropy', 'gini'], 'n_estimators' : [20, 40, 60, 80, 100],
                   'max_features' :['sqrt', 'log2']}
    rf.grid_search(parameters = param_grid, Kfold = 5)
    rf.grid_fit(X = X_train, Y = y_train)
    rf.grid_predict(X_valid, y_valid)
    ###### Voting  ###### 
    rf_best  = ensemble.RandomForestClassifier(**rf.grid.best_params_)
    knn_best = neighbors.KNeighborsClassifier(**knn.grid.best_params_)
    svc_best = svm.LinearSVC(**svc.grid.best_params_)
    votingC = ensemble.VotingClassifier(estimators=[('rf', rf_best),
                                                ('knn', knn_best)], voting='soft') 
    # traing with ensemble models 
    votingC = votingC.fit(X_train, y_train)
    predictions = votingC.predict(X_valid)
    print("Precision: {:.2f} % ".format(100*metrics.accuracy_score(y_valid, predictions)))

















