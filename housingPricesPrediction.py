
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import numpy as np

# カリフォルニアの住宅価格のデータセット
california_housing = fetch_california_housing()

# 説明変数 X
X = pd.DataFrame(california_housing.data, columns=california_housing.feature_names)

# 目的変数 y
y = pd.DataFrame(california_housing.target, columns=['MedHouseVal'])

# データを訓練用（学習用）とテスト用に分割
X_train, X_test,y_train ,y_test = train_test_split(X,y,test_size=0.3,random_state=0)

# 単回帰モデルの構築
simple_reg = LinearRegression().fit(X_train,y_train)

# 予測結果を出力
y_train_pred = simple_reg.predict(X_train)
y_test_pred = simple_reg.predict(X_test)

# モデルの評価を行う
# 平均絶対誤差（MAE：Mean Absolute Error）
mae = mean_absolute_error(y_test,y_test_pred)
# 平均二乗誤差（MSE: Mean Squared Error）
mse = mean_squared_error(y_test,y_test_pred)
# 二乗平均平方根誤差（RMSE: Root Mean Squared Error）
rmse = np.sqrt(mse)
# 決定係数（R2）
r2score = r2_score(y_test,y_test_pred)

print('テストデータスコア')
print(f"MAE ={mae}")
print(f"MSE ={mse}")
print(f"RMSE ={rmse}")
print(f"R2 ={r2score}")

# 実行後の結果
# テストデータスコア
# MAE =0.5361818140641836
# MSE =0.543148967003724
# RMSE =0.7369864089681193
# R2 =0.5926087785518775
