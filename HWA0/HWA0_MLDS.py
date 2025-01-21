import pandas as pd
#(a),(b)
df=pd.read_csv("Salaries.csv")

'''
(c)
df=df.set_index('playerID')
#Before skipping  the second row
print(df.head())
df1=df.iloc[1:]
#After Skipping the Second Row
print(df1.head())
'''

'''
(d)
Select the id of the players who are registered in ATL and HOU whose salary is
higher than one million
df2 = df[(df["teamID"].isin(['ATL', 'HOU'])) & (df["salary"] > 1000000)]
print(df2["playerID"])
'''
#(e)
df3=df[(df["teamID"])=='ATL']
df3=df3["salary"]
print(df3.describe())
