import pandas as pd
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score,mean_absolute_error


df= pd.read_csv("car_price_prediction/final.csv")
x= df[["kmdriven_sc","year_sc"]]
y = df["sellingprice_sc"]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
print(x_train)
print(y_test)



model = LinearRegression()

model.fit(x_train,y_train)

pre = model.predict(x_test)
score = r2_score(y_test,pre)
print("r2 score : ",score)


