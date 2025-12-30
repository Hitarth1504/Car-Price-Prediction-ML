import pandas as pd

df= pd.read_csv("car_price_prediction/dataset.csv")

df_label = df.copy()

df_label["owner_encoded"] = pd.get_dummies(df["owner"]).astype(int).values.tolist()
df_label["name_encoded"] = pd.get_dummies(df["name"]).astype(int).values.tolist()

df_label.to_csv("encodeddata.csv")