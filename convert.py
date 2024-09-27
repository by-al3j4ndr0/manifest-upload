import pandas as pd

data = pd.read_excel('manifiesto.xls', header=[11], usecols=[0,8,12,13], names=[
                                                                            'hbl',
                                                                            'name',
                                                                            'city',
                                                                            'state',
                                                                        ])
df = pd.DataFrame(data)
send_df = df.reindex(['hbl', 'name', 'city', 'state', 'warehouse'], axis=1)
for i in range(0, len(send_df.index)):
    send_df.at[i, "warehouse"] = "False"

print(send_df)
send_df.to_csv('manifiesto_ok.csv', index=False)