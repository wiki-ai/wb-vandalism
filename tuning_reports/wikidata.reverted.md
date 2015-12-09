# Model tuning report
- Revscoring version: 0.7.8
- Features: wb_vandalism.feature_lists.wikidata.reverted
- Date: 2015-12-09T02:40:46.902248
- Observations: 24481
- Labels: [false, true]
- Scoring: roc_auc
- Folds: 5

# Top scoring configurations
| model                      |   mean(scores) |   std(scores) | params                                                                         |
|:---------------------------|---------------:|--------------:|:-------------------------------------------------------------------------------|
| RandomForestClassifier     |          0.974 |         0.001 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=640 |
| RandomForestClassifier     |          0.974 |         0.001 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=320 |
| RandomForestClassifier     |          0.974 |         0.001 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=640    |
| RandomForestClassifier     |          0.974 |         0.001 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=320    |
| RandomForestClassifier     |          0.974 |         0.001 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=160 |
| RandomForestClassifier     |          0.974 |         0.001 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=160    |
| RandomForestClassifier     |          0.973 |         0.001 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=80  |
| RandomForestClassifier     |          0.973 |         0.001 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=80     |
| GradientBoostingClassifier |          0.972 |         0.002 | max_features="log2", n_estimators=500, max_depth=7, learning_rate=0.1          |
| GradientBoostingClassifier |          0.972 |         0.002 | max_features="log2", n_estimators=700, max_depth=7, learning_rate=0.1          |

# Models
## RandomForestClassifier
|   mean(scores) |   std(scores) | params                                                                          |
|---------------:|--------------:|:--------------------------------------------------------------------------------|
|          0.974 |         0.001 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=640  |
|          0.974 |         0.001 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=320  |
|          0.974 |         0.001 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=640     |
|          0.974 |         0.001 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=320     |
|          0.974 |         0.001 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=160  |
|          0.974 |         0.001 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=160     |
|          0.973 |         0.001 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=80   |
|          0.973 |         0.001 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=80      |
|          0.972 |         0.001 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=40      |
|          0.972 |         0.001 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=40   |
|          0.97  |         0.001 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=20   |
|          0.969 |         0.001 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=20      |
|          0.968 |         0.003 | max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=640  |
|          0.968 |         0.003 | max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=320  |
|          0.968 |         0.003 | max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=640     |
|          0.968 |         0.002 | max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=160  |
|          0.968 |         0.003 | max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=320     |
|          0.967 |         0.003 | max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=160     |
|          0.967 |         0.003 | max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=80      |
|          0.967 |         0.003 | max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=80   |
|          0.966 |         0.003 | max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=40      |
|          0.966 |         0.003 | max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=40   |
|          0.965 |         0.003 | max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=20      |
|          0.965 |         0.003 | max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=20   |
|          0.965 |         0.003 | max_features="log2", criterion="gini", min_samples_leaf=1, n_estimators=10      |
|          0.964 |         0.001 | max_features="log2", criterion="entropy", min_samples_leaf=1, n_estimators=10   |
|          0.963 |         0.003 | max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=640  |
|          0.963 |         0.003 | max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=640     |
|          0.963 |         0.003 | max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=160  |
|          0.963 |         0.003 | max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=320  |
|          0.963 |         0.003 | max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=80   |
|          0.963 |         0.003 | max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=320     |
|          0.963 |         0.004 | max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=160     |
|          0.963 |         0.003 | max_features="log2", criterion="gini", min_samples_leaf=3, n_estimators=10      |
|          0.962 |         0.003 | max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=80      |
|          0.962 |         0.003 | max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=40      |
|          0.962 |         0.003 | max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=40   |
|          0.962 |         0.003 | max_features="log2", criterion="entropy", min_samples_leaf=3, n_estimators=10   |
|          0.961 |         0.003 | max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=20   |
|          0.961 |         0.004 | max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=20      |
|          0.96  |         0.004 | max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=640  |
|          0.96  |         0.004 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=320     |
|          0.96  |         0.004 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=640     |
|          0.96  |         0.004 | max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=320  |
|          0.96  |         0.004 | max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=160  |
|          0.96  |         0.004 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=20      |
|          0.959 |         0.004 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=160     |
|          0.959 |         0.003 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=80      |
|          0.959 |         0.004 | max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=80   |
|          0.959 |         0.004 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=40      |
|          0.959 |         0.004 | max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=20   |
|          0.958 |         0.004 | max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=40   |
|          0.958 |         0.003 | max_features="log2", criterion="entropy", min_samples_leaf=5, n_estimators=10   |
|          0.956 |         0.006 | max_features="log2", criterion="gini", min_samples_leaf=5, n_estimators=10      |
|          0.955 |         0.006 | max_features="log2", criterion="gini", min_samples_leaf=7, n_estimators=10      |
|          0.955 |         0.004 | max_features="log2", criterion="entropy", min_samples_leaf=7, n_estimators=10   |
|          0.954 |         0.005 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=160 |
|          0.954 |         0.005 | max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=640    |
|          0.954 |         0.005 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=320 |
|          0.954 |         0.005 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=640 |
|          0.954 |         0.005 | max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=320    |
|          0.954 |         0.005 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=40  |
|          0.954 |         0.006 | max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=160    |
|          0.953 |         0.006 | max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=80     |
|          0.953 |         0.005 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=80  |
|          0.952 |         0.005 | max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=40     |
|          0.951 |         0.006 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=20  |
|          0.951 |         0.004 | max_features="log2", criterion="entropy", min_samples_leaf=13, n_estimators=10  |
|          0.95  |         0.006 | max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=20     |
|          0.949 |         0.006 | max_features="log2", criterion="gini", min_samples_leaf=13, n_estimators=10     |

## GaussianNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.684 |          0.01 |          |

## BernoulliNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.855 |         0.009 |          |

## LogisticRegression
|   mean(scores) |   std(scores) | params              |
|---------------:|--------------:|:--------------------|
|          0.918 |         0.004 | C=10, penalty="l1"  |
|          0.918 |         0.004 | C=10, penalty="l2"  |
|          0.918 |         0.004 | C=1, penalty="l1"   |
|          0.917 |         0.004 | C=1, penalty="l2"   |
|          0.914 |         0.004 | C=0.1, penalty="l1" |
|          0.913 |         0.005 | C=0.1, penalty="l2" |

## GradientBoostingClassifier
|   mean(scores) |   std(scores) | params                                                                 |
|---------------:|--------------:|:-----------------------------------------------------------------------|
|          0.972 |         0.002 | max_features="log2", n_estimators=500, max_depth=7, learning_rate=0.1  |
|          0.972 |         0.002 | max_features="log2", n_estimators=700, max_depth=7, learning_rate=0.1  |
|          0.971 |         0.002 | max_features="log2", n_estimators=300, max_depth=7, learning_rate=0.1  |
|          0.97  |         0.002 | max_features="log2", n_estimators=700, max_depth=5, learning_rate=0.1  |
|          0.969 |         0.002 | max_features="log2", n_estimators=500, max_depth=5, learning_rate=0.1  |
|          0.967 |         0.002 | max_features="log2", n_estimators=500, max_depth=5, learning_rate=0.5  |
|          0.966 |         0.003 | max_features="log2", n_estimators=300, max_depth=5, learning_rate=0.1  |
|          0.966 |         0.001 | max_features="log2", n_estimators=700, max_depth=3, learning_rate=0.5  |
|          0.965 |         0.003 | max_features="log2", n_estimators=100, max_depth=7, learning_rate=0.5  |
|          0.965 |         0.002 | max_features="log2", n_estimators=300, max_depth=5, learning_rate=0.5  |
|          0.965 |         0.003 | max_features="log2", n_estimators=100, max_depth=5, learning_rate=0.5  |
|          0.964 |         0.003 | max_features="log2", n_estimators=100, max_depth=7, learning_rate=0.1  |
|          0.964 |         0.003 | max_features="log2", n_estimators=500, max_depth=3, learning_rate=0.5  |
|          0.964 |         0.002 | max_features="log2", n_estimators=300, max_depth=3, learning_rate=0.5  |
|          0.962 |         0.003 | max_features="log2", n_estimators=700, max_depth=7, learning_rate=0.01 |
|          0.962 |         0.003 | max_features="log2", n_estimators=700, max_depth=3, learning_rate=0.1  |
|          0.96  |         0.003 | max_features="log2", n_estimators=500, max_depth=3, learning_rate=0.1  |
|          0.958 |         0.004 | max_features="log2", n_estimators=500, max_depth=7, learning_rate=0.01 |
|          0.958 |         0.02  | max_features="log2", n_estimators=500, max_depth=7, learning_rate=0.5  |
|          0.957 |         0.018 | max_features="log2", n_estimators=300, max_depth=7, learning_rate=0.5  |
|          0.956 |         0.005 | max_features="log2", n_estimators=100, max_depth=5, learning_rate=0.1  |
|          0.955 |         0.003 | max_features="log2", n_estimators=100, max_depth=3, learning_rate=0.5  |
|          0.955 |         0.004 | max_features="log2", n_estimators=100, max_depth=3, learning_rate=1    |
|          0.955 |         0.003 | max_features="log2", n_estimators=300, max_depth=3, learning_rate=0.1  |
|          0.954 |         0.002 | max_features="log2", n_estimators=100, max_depth=5, learning_rate=1    |
|          0.953 |         0.005 | max_features="log2", n_estimators=300, max_depth=7, learning_rate=0.01 |
|          0.952 |         0.005 | max_features="log2", n_estimators=700, max_depth=5, learning_rate=0.01 |
|          0.951 |         0.025 | max_features="log2", n_estimators=700, max_depth=5, learning_rate=0.5  |
|          0.95  |         0.008 | max_features="log2", n_estimators=300, max_depth=3, learning_rate=1    |
|          0.949 |         0.001 | max_features="log2", n_estimators=500, max_depth=1, learning_rate=1    |
|          0.948 |         0.003 | max_features="log2", n_estimators=300, max_depth=1, learning_rate=1    |
|          0.948 |         0.002 | max_features="log2", n_estimators=700, max_depth=1, learning_rate=1    |
|          0.948 |         0.002 | max_features="log2", n_estimators=700, max_depth=1, learning_rate=0.5  |
|          0.948 |         0.009 | max_features="log2", n_estimators=500, max_depth=3, learning_rate=1    |
|          0.948 |         0.003 | max_features="log2", n_estimators=500, max_depth=1, learning_rate=0.5  |
|          0.948 |         0.005 | max_features="log2", n_estimators=500, max_depth=5, learning_rate=0.01 |
|          0.945 |         0.003 | max_features="log2", n_estimators=300, max_depth=1, learning_rate=0.5  |
|          0.944 |         0.007 | max_features="log2", n_estimators=100, max_depth=7, learning_rate=0.01 |
|          0.941 |         0.007 | max_features="log2", n_estimators=300, max_depth=5, learning_rate=0.01 |
|          0.94  |         0.003 | max_features="log2", n_estimators=100, max_depth=1, learning_rate=1    |
|          0.94  |         0.007 | max_features="log2", n_estimators=100, max_depth=3, learning_rate=0.1  |
|          0.938 |         0.005 | max_features="log2", n_estimators=700, max_depth=1, learning_rate=0.1  |
|          0.937 |         0.017 | max_features="log2", n_estimators=700, max_depth=3, learning_rate=1    |
|          0.936 |         0.007 | max_features="log2", n_estimators=700, max_depth=3, learning_rate=0.01 |
|          0.935 |         0.006 | max_features="log2", n_estimators=500, max_depth=1, learning_rate=0.1  |
|          0.933 |         0.007 | max_features="log2", n_estimators=100, max_depth=1, learning_rate=0.5  |
|          0.93  |         0.008 | max_features="log2", n_estimators=100, max_depth=5, learning_rate=0.01 |
|          0.93  |         0.008 | max_features="log2", n_estimators=500, max_depth=3, learning_rate=0.01 |
|          0.926 |         0.008 | max_features="log2", n_estimators=300, max_depth=1, learning_rate=0.1  |
|          0.921 |         0.01  | max_features="log2", n_estimators=300, max_depth=3, learning_rate=0.01 |
|          0.907 |         0.076 | max_features="log2", n_estimators=100, max_depth=7, learning_rate=1    |
|          0.907 |         0.011 | max_features="log2", n_estimators=100, max_depth=1, learning_rate=0.1  |
|          0.906 |         0.013 | max_features="log2", n_estimators=100, max_depth=3, learning_rate=0.01 |
|          0.902 |         0.012 | max_features="log2", n_estimators=700, max_depth=1, learning_rate=0.01 |
|          0.896 |         0.013 | max_features="log2", n_estimators=500, max_depth=1, learning_rate=0.01 |
|          0.888 |         0.013 | max_features="log2", n_estimators=300, max_depth=1, learning_rate=0.01 |
|          0.881 |         0.013 | max_features="log2", n_estimators=100, max_depth=1, learning_rate=0.01 |
|          0.874 |         0.168 | max_features="log2", n_estimators=700, max_depth=7, learning_rate=0.5  |
|          0.869 |         0.094 | max_features="log2", n_estimators=500, max_depth=5, learning_rate=1    |
|          0.869 |         0.142 | max_features="log2", n_estimators=300, max_depth=5, learning_rate=1    |
|          0.799 |         0.118 | max_features="log2", n_estimators=300, max_depth=7, learning_rate=1    |
|          0.751 |         0.082 | max_features="log2", n_estimators=500, max_depth=7, learning_rate=1    |
|          0.635 |         0.044 | max_features="log2", n_estimators=700, max_depth=7, learning_rate=1    |
|          0     |         0     | max_features="log2", n_estimators=700, max_depth=5, learning_rate=1    |

## SVC
|   mean(scores) |   std(scores) | params                                                               |
|---------------:|--------------:|:---------------------------------------------------------------------|
|          0.938 |         0.004 | probability=true, C=10, gamma=0.0, kernel="rbf", cache_size=1000     |
|          0.929 |         0.006 | probability=true, C=1, gamma=0.0, kernel="rbf", cache_size=1000      |
|          0.915 |         0.007 | probability=true, C=10, gamma=0.001, kernel="rbf", cache_size=1000   |
|          0.913 |         0.009 | probability=true, C=0.1, gamma=0.0, kernel="rbf", cache_size=1000    |
|          0.9   |         0.01  | probability=true, C=1, gamma=0.001, kernel="rbf", cache_size=1000    |
|          0.898 |         0.01  | probability=true, C=10, gamma=0.0001, kernel="rbf", cache_size=1000  |
|          0.854 |         0.02  | probability=true, C=0.1, gamma=0.001, kernel="rbf", cache_size=1000  |
|          0.853 |         0.02  | probability=true, C=1, gamma=0.0001, kernel="rbf", cache_size=1000   |
|          0.829 |         0.023 | probability=true, C=0.1, gamma=0.0001, kernel="rbf", cache_size=1000 |

