import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
plt.rc("font", family = "Malgun Gothic")
df = sns.load_dataset("penguins")
df.columns = ['종','섬','부리길이_mm','부리너비_mm','날개길이_mm','체중_g','성별']
print(df.head())
print(df.isnull())
print(df.isnull().sum())
df = df.dropna()
print(df.isnull().sum())
print(df["종"].value_counts())
print(df["성별"].value_counts())
df = df[["종","부리길이_mm","날개길이_mm","성별"]]
print(df)
sns.scatterplot(x = "부리길이_mm", y = "날개길이_mm",hue = '종', style = '성별', data = df)
plt.xlabel("부리길이(mm)", size = 20)
plt.ylabel("날개길이(mm)", size = 20)

plt.show()
