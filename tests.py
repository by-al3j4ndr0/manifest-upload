import pandas as pd

data = pd.read_csv('manifiesto_ok.csv')
df = pd.DataFrame(data)
false_df = pd.DataFrame(columns=('hbl', 'name', 'city', 'state', 'warehouse'))

query = df.loc[df["warehouse"] != True] 
df_final = pd.concat([false_df, query])


print(df_final)

    