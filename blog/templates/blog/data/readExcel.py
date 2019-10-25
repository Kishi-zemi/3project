import pandas as pd

df = pd.read_excel('H30.xlsx', index=False, dytpe='object')

fileLen = len(df)
print(fileLen, "行読み込み完了")

df = df.drop(columns = '計上所属')
df = df.drop(columns = '所属コード')
df = df.drop(columns = '道路形状')
df = df.drop(columns = '死者数')
df = df.drop(columns = '負傷者数')

df.to_excel('H30.xlsx', index=False)
