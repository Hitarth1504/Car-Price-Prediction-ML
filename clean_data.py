import pandas as pd
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error
from sklearn.ensemble import RandomForestRegressor

df= pd.read_csv("car_price_prediction/dataset.csv")


#target attributes x =kmdriven,year,owner   y = sellingprice

df["owner_encoded"] = pd.get_dummies(df["owner"]).astype(int).values.tolist()

l = ["kmdriven","year",""]


x= df[["kmdriven","year"]]
y = df["sellingprice"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
print(x_train)
print(y_test)
model = RandomForestRegressor(n_estimators=200, random_state=42)

model.fit(x_train,y_train)

pre = model.predict(x_test)
score = r2_score(y_test,pre)
print("r2 score : ",score)

i = float(input("enter km :"))
y = float(input("enter year : "))

pred = model.predict([[i,y]])

print(f"as your km{i} and year {y} price was likly : {pred}")