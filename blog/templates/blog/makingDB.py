import sqlite3
import pandas as pd
import pandas.io.sql as psql

df1 = pd.read_csv("data/H30.csv")
df1 = df1.dropna()

df2 = pd.read_csv("data/H29.csv")
df2 = df2.dropna()

df3 = pd.read_csv("data/H28.csv")
df3 = df3.dropna()

df = pd.concat([df1, df2, df3], ignore_index=True, sort = False, keys=['df1','df2','df3'])

dbname = 'h28_30.db'

conn = sqlite3.connect(dbname)
cur = conn.cursor()


df.to_sql('sample', conn, if_exists='replace')


dfold = psql.read_sql("SELECT * FROM sample WHERE (甲_年齢 = '65～74歳') OR (甲_年齢 = '75歳以上')", conn)
dfold.to_sql('old', conn, if_exists='replace')

cur.close()
conn.close()
