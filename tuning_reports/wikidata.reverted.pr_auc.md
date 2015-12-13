# Model tuning report
- Revscoring version: 0.7.8
- Features: wb_vandalism.feature_lists.wikidata.reverted
- Date: 2015-12-09T05:47:45.393043
- Observations: 24481
- Labels: [false, true]
- Scoring: make_scorer(pr_auc_score, needs_proba=True)
- Folds: 5

# Top scoring configurations
| model                  |   mean(scores) |   std(scores) | params                                                                         |
|:-----------------------|---------------:|--------------:|:-------------------------------------------------------------------------------|
| RandomForestClassifier |          0.971 |         0.002 | max_features="log2", criterion="entropy", n_estimators=640, min_samples_leaf=1 |
| RandomForestClassifier |          0.97  |         0.001 | max_features="log2", criterion="entropy", n_estimators=320, min_samples_leaf=1 |
| RandomForestClassifier |          0.97  |         0.001 | max_features="log2", criterion="gini", n_estimators=160, min_samples_leaf=1    |
| RandomForestClassifier |          0.97  |         0.001 | max_features="log2", criterion="entropy", n_estimators=160, min_samples_leaf=1 |
| RandomForestClassifier |          0.97  |         0.002 | max_features="log2", criterion="gini", n_estimators=320, min_samples_leaf=1    |
| RandomForestClassifier |          0.97  |         0.001 | max_features="log2", criterion="gini", n_estimators=640, min_samples_leaf=1    |
| RandomForestClassifier |          0.97  |         0.001 | max_features="log2", criterion="entropy", n_estimators=80, min_samples_leaf=1  |
| RandomForestClassifier |          0.97  |         0.001 | max_features="log2", criterion="gini", n_estimators=80, min_samples_leaf=1     |
| RandomForestClassifier |          0.969 |         0.001 | max_features="log2", criterion="entropy", n_estimators=40, min_samples_leaf=1  |
| RandomForestClassifier |          0.969 |         0.002 | max_features="log2", criterion="gini", n_estimators=40, min_samples_leaf=1     |

# Models
## BernoulliNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.848 |         0.011 |          |

## RandomForestClassifier
|   mean(scores) |   std(scores) | params                                                                          |
|---------------:|--------------:|:--------------------------------------------------------------------------------|
|          0.971 |         0.002 | max_features="log2", criterion="entropy", n_estimators=640, min_samples_leaf=1  |
|          0.97  |         0.001 | max_features="log2", criterion="entropy", n_estimators=320, min_samples_leaf=1  |
|          0.97  |         0.001 | max_features="log2", criterion="gini", n_estimators=160, min_samples_leaf=1     |
|          0.97  |         0.001 | max_features="log2", criterion="entropy", n_estimators=160, min_samples_leaf=1  |
|          0.97  |         0.002 | max_features="log2", criterion="gini", n_estimators=320, min_samples_leaf=1     |
|          0.97  |         0.001 | max_features="log2", criterion="gini", n_estimators=640, min_samples_leaf=1     |
|          0.97  |         0.001 | max_features="log2", criterion="entropy", n_estimators=80, min_samples_leaf=1   |
|          0.97  |         0.001 | max_features="log2", criterion="gini", n_estimators=80, min_samples_leaf=1      |
|          0.969 |         0.001 | max_features="log2", criterion="entropy", n_estimators=40, min_samples_leaf=1   |
|          0.969 |         0.002 | max_features="log2", criterion="gini", n_estimators=40, min_samples_leaf=1      |
|          0.967 |         0.002 | max_features="log2", criterion="entropy", n_estimators=20, min_samples_leaf=1   |
|          0.966 |         0.002 | max_features="log2", criterion="gini", n_estimators=20, min_samples_leaf=1      |
|          0.964 |         0.003 | max_features="log2", criterion="gini", n_estimators=640, min_samples_leaf=3     |
|          0.964 |         0.003 | max_features="log2", criterion="entropy", n_estimators=640, min_samples_leaf=3  |
|          0.964 |         0.003 | max_features="log2", criterion="gini", n_estimators=320, min_samples_leaf=3     |
|          0.964 |         0.003 | max_features="log2", criterion="entropy", n_estimators=160, min_samples_leaf=3  |
|          0.963 |         0.003 | max_features="log2", criterion="gini", n_estimators=160, min_samples_leaf=3     |
|          0.963 |         0.003 | max_features="log2", criterion="entropy", n_estimators=320, min_samples_leaf=3  |
|          0.963 |         0.003 | max_features="log2", criterion="gini", n_estimators=80, min_samples_leaf=3      |
|          0.962 |         0.003 | max_features="log2", criterion="entropy", n_estimators=80, min_samples_leaf=3   |
|          0.962 |         0.003 | max_features="log2", criterion="gini", n_estimators=40, min_samples_leaf=3      |
|          0.962 |         0.003 | max_features="log2", criterion="entropy", n_estimators=40, min_samples_leaf=3   |
|          0.962 |         0.002 | max_features="log2", criterion="gini", n_estimators=10, min_samples_leaf=1      |
|          0.961 |         0.001 | max_features="log2", criterion="entropy", n_estimators=10, min_samples_leaf=1   |
|          0.96  |         0.003 | max_features="log2", criterion="entropy", n_estimators=20, min_samples_leaf=3   |
|          0.959 |         0.003 | max_features="log2", criterion="gini", n_estimators=20, min_samples_leaf=3      |
|          0.959 |         0.004 | max_features="log2", criterion="entropy", n_estimators=10, min_samples_leaf=3   |
|          0.959 |         0.003 | max_features="log2", criterion="entropy", n_estimators=640, min_samples_leaf=5  |
|          0.959 |         0.004 | max_features="log2", criterion="entropy", n_estimators=320, min_samples_leaf=5  |
|          0.959 |         0.004 | max_features="log2", criterion="gini", n_estimators=160, min_samples_leaf=5     |
|          0.959 |         0.004 | max_features="log2", criterion="gini", n_estimators=640, min_samples_leaf=5     |
|          0.958 |         0.004 | max_features="log2", criterion="gini", n_estimators=320, min_samples_leaf=5     |
|          0.958 |         0.003 | max_features="log2", criterion="entropy", n_estimators=80, min_samples_leaf=5   |
|          0.958 |         0.003 | max_features="log2", criterion="gini", n_estimators=80, min_samples_leaf=5      |
|          0.958 |         0.003 | max_features="log2", criterion="entropy", n_estimators=160, min_samples_leaf=5  |
|          0.957 |         0.003 | max_features="log2", criterion="entropy", n_estimators=40, min_samples_leaf=5   |
|          0.957 |         0.004 | max_features="log2", criterion="gini", n_estimators=40, min_samples_leaf=5      |
|          0.956 |         0.005 | max_features="log2", criterion="gini", n_estimators=10, min_samples_leaf=3      |
|          0.955 |         0.003 | max_features="log2", criterion="gini", n_estimators=20, min_samples_leaf=5      |
|          0.955 |         0.004 | max_features="log2", criterion="entropy", n_estimators=640, min_samples_leaf=7  |
|          0.955 |         0.004 | max_features="log2", criterion="gini", n_estimators=640, min_samples_leaf=7     |
|          0.955 |         0.004 | max_features="log2", criterion="entropy", n_estimators=320, min_samples_leaf=7  |
|          0.955 |         0.004 | max_features="log2", criterion="gini", n_estimators=80, min_samples_leaf=7      |
|          0.955 |         0.004 | max_features="log2", criterion="gini", n_estimators=160, min_samples_leaf=7     |
|          0.955 |         0.004 | max_features="log2", criterion="entropy", n_estimators=160, min_samples_leaf=7  |
|          0.955 |         0.005 | max_features="log2", criterion="gini", n_estimators=320, min_samples_leaf=7     |
|          0.955 |         0.004 | max_features="log2", criterion="entropy", n_estimators=40, min_samples_leaf=7   |
|          0.954 |         0.004 | max_features="log2", criterion="entropy", n_estimators=80, min_samples_leaf=7   |
|          0.954 |         0.005 | max_features="log2", criterion="entropy", n_estimators=20, min_samples_leaf=5   |
|          0.954 |         0.004 | max_features="log2", criterion="gini", n_estimators=40, min_samples_leaf=7      |
|          0.953 |         0.004 | max_features="log2", criterion="entropy", n_estimators=20, min_samples_leaf=7   |
|          0.953 |         0.003 | max_features="log2", criterion="entropy", n_estimators=10, min_samples_leaf=5   |
|          0.953 |         0.005 | max_features="log2", criterion="gini", n_estimators=20, min_samples_leaf=7      |
|          0.951 |         0.006 | max_features="log2", criterion="gini", n_estimators=10, min_samples_leaf=5      |
|          0.95  |         0.005 | max_features="log2", criterion="gini", n_estimators=10, min_samples_leaf=7      |
|          0.949 |         0.005 | max_features="log2", criterion="entropy", n_estimators=10, min_samples_leaf=7   |
|          0.949 |         0.005 | max_features="log2", criterion="entropy", n_estimators=320, min_samples_leaf=13 |
|          0.949 |         0.006 | max_features="log2", criterion="gini", n_estimators=640, min_samples_leaf=13    |
|          0.949 |         0.005 | max_features="log2", criterion="entropy", n_estimators=160, min_samples_leaf=13 |
|          0.949 |         0.005 | max_features="log2", criterion="entropy", n_estimators=80, min_samples_leaf=13  |
|          0.949 |         0.005 | max_features="log2", criterion="entropy", n_estimators=640, min_samples_leaf=13 |
|          0.949 |         0.006 | max_features="log2", criterion="gini", n_estimators=320, min_samples_leaf=13    |
|          0.949 |         0.006 | max_features="log2", criterion="gini", n_estimators=80, min_samples_leaf=13     |
|          0.948 |         0.006 | max_features="log2", criterion="gini", n_estimators=160, min_samples_leaf=13    |
|          0.947 |         0.005 | max_features="log2", criterion="entropy", n_estimators=40, min_samples_leaf=13  |
|          0.947 |         0.005 | max_features="log2", criterion="gini", n_estimators=40, min_samples_leaf=13     |
|          0.946 |         0.005 | max_features="log2", criterion="gini", n_estimators=20, min_samples_leaf=13     |
|          0.946 |         0.005 | max_features="log2", criterion="gini", n_estimators=10, min_samples_leaf=13     |
|          0.945 |         0.006 | max_features="log2", criterion="entropy", n_estimators=20, min_samples_leaf=13  |
|          0.942 |         0.006 | max_features="log2", criterion="entropy", n_estimators=10, min_samples_leaf=13  |

## SVC
|   mean(scores) |   std(scores) | params                                                               |
|---------------:|--------------:|:---------------------------------------------------------------------|
|          0.903 |         0.007 | C=10, kernel="rbf", cache_size=1000, gamma=0.0, probability=true     |
|          0.897 |         0.011 | C=10, kernel="rbf", cache_size=1000, gamma=0.001, probability=true   |
|          0.893 |         0.011 | C=10, kernel="rbf", cache_size=1000, gamma=0.0001, probability=true  |
|          0.89  |         0.012 | C=1, kernel="rbf", cache_size=1000, gamma=0.001, probability=true    |
|          0.889 |         0.01  | C=1, kernel="rbf", cache_size=1000, gamma=0.0, probability=true      |
|          0.873 |         0.013 | C=0.1, kernel="rbf", cache_size=1000, gamma=0.0, probability=true    |
|          0.858 |         0.017 | C=0.1, kernel="rbf", cache_size=1000, gamma=0.001, probability=true  |
|          0.857 |         0.017 | C=1, kernel="rbf", cache_size=1000, gamma=0.0001, probability=true   |
|          0.844 |         0.019 | C=0.1, kernel="rbf", cache_size=1000, gamma=0.0001, probability=true |

## GradientBoostingClassifier
|   mean(scores) |   std(scores) | params                                                                 |
|---------------:|--------------:|:-----------------------------------------------------------------------|
|          0.967 |         0.003 | max_features="log2", max_depth=7, learning_rate=0.1, n_estimators=500  |
|          0.967 |         0.003 | max_features="log2", max_depth=7, learning_rate=0.1, n_estimators=700  |
|          0.966 |         0.002 | max_features="log2", max_depth=7, learning_rate=0.1, n_estimators=300  |
|          0.966 |         0.003 | max_features="log2", max_depth=5, learning_rate=0.1, n_estimators=700  |
|          0.964 |         0.004 | max_features="log2", max_depth=5, learning_rate=0.1, n_estimators=500  |
|          0.962 |         0.004 | max_features="log2", max_depth=7, learning_rate=0.5, n_estimators=500  |
|          0.962 |         0.004 | max_features="log2", max_depth=5, learning_rate=0.1, n_estimators=300  |
|          0.96  |         0.004 | max_features="log2", max_depth=7, learning_rate=0.1, n_estimators=100  |
|          0.96  |         0.004 | max_features="log2", max_depth=5, learning_rate=0.5, n_estimators=300  |
|          0.959 |         0.006 | max_features="log2", max_depth=3, learning_rate=0.5, n_estimators=700  |
|          0.958 |         0.004 | max_features="log2", max_depth=7, learning_rate=0.01, n_estimators=700 |
|          0.958 |         0.002 | max_features="log2", max_depth=7, learning_rate=0.5, n_estimators=100  |
|          0.957 |         0.004 | max_features="log2", max_depth=5, learning_rate=0.5, n_estimators=100  |
|          0.957 |         0.004 | max_features="log2", max_depth=3, learning_rate=0.1, n_estimators=700  |
|          0.954 |         0.007 | max_features="log2", max_depth=3, learning_rate=0.5, n_estimators=300  |
|          0.954 |         0.006 | max_features="log2", max_depth=3, learning_rate=0.5, n_estimators=500  |
|          0.954 |         0.004 | max_features="log2", max_depth=3, learning_rate=0.1, n_estimators=500  |
|          0.954 |         0.005 | max_features="log2", max_depth=7, learning_rate=0.01, n_estimators=500 |
|          0.95  |         0.013 | max_features="log2", max_depth=7, learning_rate=0.5, n_estimators=300  |
|          0.95  |         0.005 | max_features="log2", max_depth=3, learning_rate=0.5, n_estimators=100  |
|          0.95  |         0.005 | max_features="log2", max_depth=5, learning_rate=0.1, n_estimators=100  |
|          0.948 |         0.005 | max_features="log2", max_depth=3, learning_rate=0.1, n_estimators=300  |
|          0.947 |         0.006 | max_features="log2", max_depth=7, learning_rate=0.01, n_estimators=300 |
|          0.946 |         0.006 | max_features="log2", max_depth=5, learning_rate=0.01, n_estimators=700 |
|          0.942 |         0.026 | max_features="log2", max_depth=5, learning_rate=0.5, n_estimators=500  |
|          0.941 |         0.006 | max_features="log2", max_depth=5, learning_rate=0.01, n_estimators=500 |
|          0.941 |         0.003 | max_features="log2", max_depth=3, learning_rate=1, n_estimators=100    |
|          0.94  |         0.004 | max_features="log2", max_depth=1, learning_rate=0.5, n_estimators=700  |
|          0.938 |         0.008 | max_features="log2", max_depth=7, learning_rate=0.01, n_estimators=100 |
|          0.938 |         0.004 | max_features="log2", max_depth=3, learning_rate=1, n_estimators=300    |
|          0.938 |         0.003 | max_features="log2", max_depth=1, learning_rate=0.5, n_estimators=500  |
|          0.938 |         0.003 | max_features="log2", max_depth=5, learning_rate=1, n_estimators=100    |
|          0.938 |         0.003 | max_features="log2", max_depth=1, learning_rate=1, n_estimators=300    |
|          0.936 |         0.005 | max_features="log2", max_depth=1, learning_rate=0.5, n_estimators=300  |
|          0.935 |         0.008 | max_features="log2", max_depth=1, learning_rate=1, n_estimators=700    |
|          0.935 |         0.008 | max_features="log2", max_depth=5, learning_rate=0.01, n_estimators=300 |
|          0.933 |         0.004 | max_features="log2", max_depth=1, learning_rate=1, n_estimators=500    |
|          0.932 |         0.007 | max_features="log2", max_depth=3, learning_rate=0.1, n_estimators=100  |
|          0.932 |         0.007 | max_features="log2", max_depth=1, learning_rate=1, n_estimators=100    |
|          0.928 |         0.009 | max_features="log2", max_depth=3, learning_rate=0.01, n_estimators=700 |
|          0.928 |         0.007 | max_features="log2", max_depth=1, learning_rate=0.1, n_estimators=700  |
|          0.927 |         0.015 | max_features="log2", max_depth=7, learning_rate=1, n_estimators=100    |
|          0.924 |         0.008 | max_features="log2", max_depth=1, learning_rate=0.1, n_estimators=500  |
|          0.924 |         0.007 | max_features="log2", max_depth=1, learning_rate=0.5, n_estimators=100  |
|          0.923 |         0.009 | max_features="log2", max_depth=5, learning_rate=0.01, n_estimators=100 |
|          0.922 |         0.01  | max_features="log2", max_depth=3, learning_rate=0.01, n_estimators=500 |
|          0.921 |         0.083 | max_features="log2", max_depth=7, learning_rate=0.5, n_estimators=700  |
|          0.919 |         0.023 | max_features="log2", max_depth=3, learning_rate=1, n_estimators=500    |
|          0.917 |         0.01  | max_features="log2", max_depth=1, learning_rate=0.1, n_estimators=300  |
|          0.915 |         0.01  | max_features="log2", max_depth=3, learning_rate=0.01, n_estimators=300 |
|          0.913 |         0.026 | max_features="log2", max_depth=3, learning_rate=1, n_estimators=700    |
|          0.908 |         0.079 | max_features="log2", max_depth=5, learning_rate=0.5, n_estimators=700  |
|          0.904 |         0.04  | max_features="log2", max_depth=5, learning_rate=1, n_estimators=300    |
|          0.901 |         0.011 | max_features="log2", max_depth=3, learning_rate=0.01, n_estimators=100 |
|          0.894 |         0.012 | max_features="log2", max_depth=1, learning_rate=0.01, n_estimators=700 |
|          0.893 |         0.013 | max_features="log2", max_depth=1, learning_rate=0.1, n_estimators=100  |
|          0.886 |         0.012 | max_features="log2", max_depth=1, learning_rate=0.01, n_estimators=500 |
|          0.876 |         0.016 | max_features="log2", max_depth=1, learning_rate=0.01, n_estimators=300 |
|          0.871 |         0.064 | max_features="log2", max_depth=5, learning_rate=1, n_estimators=700    |
|          0.851 |         0.024 | max_features="log2", max_depth=1, learning_rate=0.01, n_estimators=100 |
|          0.834 |         0.073 | max_features="log2", max_depth=7, learning_rate=1, n_estimators=300    |
|          0.794 |         0.072 | max_features="log2", max_depth=5, learning_rate=1, n_estimators=500    |
|          0.727 |         0.013 | max_features="log2", max_depth=7, learning_rate=1, n_estimators=700    |
|          0.669 |         0.068 | max_features="log2", max_depth=7, learning_rate=1, n_estimators=500    |

## GaussianNB
|   mean(scores) |   std(scores) | params   |
|---------------:|--------------:|:---------|
|          0.782 |         0.009 |          |

## LogisticRegression
|   mean(scores) |   std(scores) | params              |
|---------------:|--------------:|:--------------------|
|          0.906 |         0.007 | C=10, penalty="l1"  |
|          0.906 |         0.007 | C=10, penalty="l2"  |
|          0.906 |         0.007 | C=1, penalty="l2"   |
|          0.906 |         0.007 | C=1, penalty="l1"   |
|          0.903 |         0.006 | C=0.1, penalty="l1" |
|          0.901 |         0.006 | C=0.1, penalty="l2" |

