import pandas as pd
 
df_clean = pd.read_csv("car_price_prediction/dataset.csv")
df_scal = pd.read_csv("car_price_prediction/scaldata.csv")

df_final = pd.concat([df_clean,df_scal],axis=1)
df_final.to_csv("final.csv")