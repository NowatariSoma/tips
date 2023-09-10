import numpy as np
import pandas as pd
from sklearn import preprocessing, kernel_ridge
from sklearn.model_selection import KFold, GridSearchCV

# csvファイルの読み込み
read_X = pd.read_csv('./data/recipe.csv').drop(columns = 'Number')
read_Y = pd.read_csv('./data/profile.csv').drop(columns = 'Number')

# データ抽出
train_X = read_X.astype(float).values
train_Y = read_Y.astype(float).values

print(train_X)

# 標準化
scaler_X = preprocessing.StandardScaler()
scaler_Y = preprocessing.StandardScaler()
scaled_train_X = scaler_X.fit_transform(train_X)
scaled_train_Y = scaler_Y.fit_transform(train_Y)

# k-foldクロスバリデーションの分割数N, グリッドサーチ探索範囲
fold_number = 5
k_fold = KFold(n_splits = fold_number, shuffle = True, random_state = 10)
hyperparameters = {'alpha': np.arange(0.0, 1.0, 0.01), 'gamma': np.logspace(-2, 2, 100)}

# グリッドサーチ
model = GridSearchCV(kernel_ridge.KernelRidge(kernel = 'rbf'), param_grid = hyperparameters, cv = k_fold, return_train_score = True)
model.fit(scaled_train_X, scaled_train_Y)

# グリッドサーチの結果の確認
df_cv_results = pd.DataFrame(model.cv_results_)
print(df_cv_results.loc[model.best_index_])
print(model.best_score_)
print(model.best_params_)
best_model = model.best_estimator_
best_model.fit(scaled_train_X, scaled_train_Y)
