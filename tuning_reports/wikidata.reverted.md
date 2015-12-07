# Model tuning report
- Revscoring version: 0.7.7
- Features: wb_vandalism.feature_lists.wikidata.reverted
- Date: 2015-12-06T20:08:40.325995
- Observations: 24481
- Labels: [false, true]
- Scoring: roc_auc
- Folds: 5

# Top scoring configurations
model                         mean(scores)    std(scores)  params
--------------------------  --------------  -------------  ------------------------------------------------------------------------------
RandomForestClassifier               0.974              0  max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=640
RandomForestClassifier               0.974              0  max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=640
RandomForestClassifier               0.974              0  max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=320
RandomForestClassifier               0.974              0  max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=320
RandomForestClassifier               0.974              0  max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=160
RandomForestClassifier               0.973              0  max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=160
RandomForestClassifier               0.973              0  max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=80
RandomForestClassifier               0.973              0  max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=80
GradientBoostingClassifier           0.972              0  max_depth=7, learning_rate=0.1, max_features="log2", n_estimators=700
RandomForestClassifier               0.972              0  max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=40

# Models
## SVC
  mean(scores)    std(scores)  params
--------------  -------------  --------------------------------------------------------------------
         0.938              0  C=10, cache_size=1000, kernel="rbf", probability=true, gamma=0.0
         0.929              0  C=1, cache_size=1000, kernel="rbf", probability=true, gamma=0.0
         0.915              0  C=10, cache_size=1000, kernel="rbf", probability=true, gamma=0.001
         0.913              0  C=0.1, cache_size=1000, kernel="rbf", probability=true, gamma=0.0
         0.9                0  C=1, cache_size=1000, kernel="rbf", probability=true, gamma=0.001
         0.898              0  C=10, cache_size=1000, kernel="rbf", probability=true, gamma=0.0001
         0.854              0  C=0.1, cache_size=1000, kernel="rbf", probability=true, gamma=0.001
         0.853              0  C=1, cache_size=1000, kernel="rbf", probability=true, gamma=0.0001
         0.829              0  C=0.1, cache_size=1000, kernel="rbf", probability=true, gamma=0.0001

## LogisticRegression
  mean(scores)    std(scores)  params
--------------  -------------  -------------------
         0.918              0  C=10, penalty="l1"
         0.918              0  C=10, penalty="l2"
         0.918              0  C=1, penalty="l1"
         0.917              0  C=1, penalty="l2"
         0.914              0  C=0.1, penalty="l1"
         0.913              0  C=0.1, penalty="l2"

## BernoulliNB
  mean(scores)    std(scores)  params
--------------  -------------  --------
         0.855              0

## GradientBoostingClassifier
  mean(scores)    std(scores)  params
--------------  -------------  ----------------------------------------------------------------------
         0.972              0  max_depth=7, learning_rate=0.1, max_features="log2", n_estimators=700
         0.972              0  max_depth=7, learning_rate=0.1, max_features="log2", n_estimators=500
         0.972              0  max_depth=7, learning_rate=0.1, max_features="log2", n_estimators=300
         0.97               0  max_depth=5, learning_rate=0.1, max_features="log2", n_estimators=700
         0.969              0  max_depth=5, learning_rate=0.1, max_features="log2", n_estimators=500
         0.968              0  max_depth=7, learning_rate=0.5, max_features="log2", n_estimators=700
         0.967              0  max_depth=7, learning_rate=0.5, max_features="log2", n_estimators=500
         0.967              0  max_depth=7, learning_rate=0.5, max_features="log2", n_estimators=300
         0.966              0  max_depth=3, learning_rate=0.5, max_features="log2", n_estimators=700
         0.966              0  max_depth=7, learning_rate=0.5, max_features="log2", n_estimators=100
         0.966              0  max_depth=5, learning_rate=0.1, max_features="log2", n_estimators=300
         0.966              0  max_depth=5, learning_rate=0.5, max_features="log2", n_estimators=300
         0.965              0  max_depth=5, learning_rate=0.5, max_features="log2", n_estimators=500
         0.964              0  max_depth=7, learning_rate=0.1, max_features="log2", n_estimators=100
         0.964              0  max_depth=5, learning_rate=0.5, max_features="log2", n_estimators=100
         0.963              0  max_depth=3, learning_rate=0.5, max_features="log2", n_estimators=500
         0.963              0  max_depth=3, learning_rate=0.5, max_features="log2", n_estimators=300
         0.962              0  max_depth=3, learning_rate=0.1, max_features="log2", n_estimators=700
         0.962              0  max_depth=7, learning_rate=0.01, max_features="log2", n_estimators=700
         0.96               0  max_depth=3, learning_rate=0.1, max_features="log2", n_estimators=500
         0.959              0  max_depth=7, learning_rate=0.01, max_features="log2", n_estimators=500
         0.956              0  max_depth=5, learning_rate=0.1, max_features="log2", n_estimators=100
         0.955              0  max_depth=3, learning_rate=0.5, max_features="log2", n_estimators=100
         0.955              0  max_depth=3, learning_rate=0.1, max_features="log2", n_estimators=300
         0.954              0  max_depth=3, learning_rate=1, max_features="log2", n_estimators=100
         0.953              0  max_depth=7, learning_rate=0.01, max_features="log2", n_estimators=300
         0.953              0  max_depth=3, learning_rate=1, max_features="log2", n_estimators=300
         0.952              0  max_depth=5, learning_rate=0.01, max_features="log2", n_estimators=700
         0.952              0  max_depth=5, learning_rate=1, max_features="log2", n_estimators=100
         0.949              0  max_depth=1, learning_rate=1, max_features="log2", n_estimators=500
         0.948              0  max_depth=1, learning_rate=0.5, max_features="log2", n_estimators=700
         0.948              0  max_depth=1, learning_rate=1, max_features="log2", n_estimators=700
         0.948              0  max_depth=5, learning_rate=0.01, max_features="log2", n_estimators=500
         0.948              0  max_depth=1, learning_rate=1, max_features="log2", n_estimators=300
         0.947              0  max_depth=1, learning_rate=0.5, max_features="log2", n_estimators=500
         0.945              0  max_depth=1, learning_rate=0.5, max_features="log2", n_estimators=300
         0.944              0  max_depth=7, learning_rate=0.01, max_features="log2", n_estimators=100
         0.941              0  max_depth=5, learning_rate=0.01, max_features="log2", n_estimators=300
         0.941              0  max_depth=5, learning_rate=0.5, max_features="log2", n_estimators=700
         0.94               0  max_depth=3, learning_rate=0.1, max_features="log2", n_estimators=100
         0.939              0  max_depth=1, learning_rate=1, max_features="log2", n_estimators=100
         0.938              0  max_depth=1, learning_rate=0.1, max_features="log2", n_estimators=700
         0.936              0  max_depth=3, learning_rate=1, max_features="log2", n_estimators=500
         0.936              0  max_depth=3, learning_rate=0.01, max_features="log2", n_estimators=700
         0.934              0  max_depth=1, learning_rate=0.1, max_features="log2", n_estimators=500
         0.933              0  max_depth=3, learning_rate=1, max_features="log2", n_estimators=700
         0.933              0  max_depth=1, learning_rate=0.5, max_features="log2", n_estimators=100
         0.93               0  max_depth=5, learning_rate=0.01, max_features="log2", n_estimators=100
         0.93               0  max_depth=3, learning_rate=0.01, max_features="log2", n_estimators=500
         0.927              0  max_depth=1, learning_rate=0.1, max_features="log2", n_estimators=300
         0.925              0  max_depth=7, learning_rate=1, max_features="log2", n_estimators=100
         0.922              0  max_depth=3, learning_rate=0.01, max_features="log2", n_estimators=300
         0.92               0  max_depth=5, learning_rate=1, max_features="log2", n_estimators=300
         0.909              0  max_depth=1, learning_rate=0.1, max_features="log2", n_estimators=100
         0.909              0  max_depth=3, learning_rate=0.01, max_features="log2", n_estimators=100
         0.902              0  max_depth=1, learning_rate=0.01, max_features="log2", n_estimators=700
         0.896              0  max_depth=1, learning_rate=0.01, max_features="log2", n_estimators=500
         0.888              0  max_depth=1, learning_rate=0.01, max_features="log2", n_estimators=300
         0.877              0  max_depth=1, learning_rate=0.01, max_features="log2", n_estimators=100
         0.844              0  max_depth=5, learning_rate=1, max_features="log2", n_estimators=500
         0.806              0  max_depth=5, learning_rate=1, max_features="log2", n_estimators=700
         0.668              0  max_depth=7, learning_rate=1, max_features="log2", n_estimators=700
         0                  0  max_depth=7, learning_rate=1, max_features="log2", n_estimators=300
         0                  0  max_depth=7, learning_rate=1, max_features="log2", n_estimators=500

## GaussianNB
  mean(scores)    std(scores)  params
--------------  -------------  --------
         0.684              0

## RandomForestClassifier
  mean(scores)    std(scores)  params
--------------  -------------  -------------------------------------------------------------------------------
         0.974              0  max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=640
         0.974              0  max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=640
         0.974              0  max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=320
         0.974              0  max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=320
         0.974              0  max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=160
         0.973              0  max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=160
         0.973              0  max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=80
         0.973              0  max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=80
         0.972              0  max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=40
         0.972              0  max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=40
         0.97               0  max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=20
         0.969              0  max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=20
         0.968              0  max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=640
         0.968              0  max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=320
         0.968              0  max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=640
         0.967              0  max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=320
         0.967              0  max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=160
         0.967              0  max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=160
         0.967              0  max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=80
         0.967              0  max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=80
         0.966              0  max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=40
         0.965              0  max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=20
         0.965              0  max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=40
         0.965              0  max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=10
         0.965              0  max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=20
         0.964              0  max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=10
         0.963              0  max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=320
         0.963              0  max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=640
         0.963              0  max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=640
         0.963              0  max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=160
         0.963              0  max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=160
         0.963              0  max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=80
         0.963              0  max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=320
         0.963              0  max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=10
         0.962              0  max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=80
         0.962              0  max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=40
         0.962              0  max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=40
         0.962              0  max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=10
         0.96               0  max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=20
         0.96               0  max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=640
         0.96               0  max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=640
         0.96               0  max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=320
         0.96               0  max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=320
         0.96               0  max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=160
         0.96               0  max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=80
         0.959              0  max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=160
         0.959              0  max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=80
         0.959              0  max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=20
         0.959              0  max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=40
         0.959              0  max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=40
         0.957              0  max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=10
         0.957              0  max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=20
         0.957              0  max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=10
         0.957              0  max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=20
         0.954              0  max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=10
         0.954              0  max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=320
         0.954              0  max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=640
         0.954              0  max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=10
         0.954              0  max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=320
         0.954              0  max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=80
         0.954              0  max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=640
         0.954              0  max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=160
         0.954              0  max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=160
         0.954              0  max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=80
         0.953              0  max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=40
         0.953              0  max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=40
         0.952              0  max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=20
         0.949              0  max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=20
         0.948              0  max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=10
         0.946              0  max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=10

