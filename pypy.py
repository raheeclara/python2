import pandas as pd
import matplotlib.pyplot as plt

'''
df1 = pd.read_csv("sleeping_hours.csv", encoding = "euc-kr",header = [0, 1])
print(df1)
df2 = pd.read_csv("sleeping_hours.csv", encoding = "euc-kr",index_col = [0, 1])
print(df2)
df3 = pd.read_csv("sleeping_hours.csv", encoding = "euc-kr",header = [0, 1],index_col = [0, 1])
df3 = df3.T
df4 = df3.rename_axis(index = ["연도","수면시간"])
print(df4)
'''

df = pd.read_csv("sleeping_hours.csv", encoding = "euc-kr",header = [0, 1],index_col = [0, 1])
df = df.T
df = df.rename_axis(index = ["연도","수면시간"])

times = ["5시간 미만","5~6시간","6~7시간","7~8시간","8~9시간","9시간 이상"]

high_2019 = df["학업성적"].iloc[6:,0]
middle_2019 = df["학업성적"].iloc[6:,1]
low_2019 = df["학업성적"].iloc[6:,2]

plt.rc("font", family = "Malgun Gothic")
plt.title("2019년 학원 성적별 수면 시간")
plt.plot(times, high_2019, label = "상")
plt.plot(times, middle_2019, label = "중")
plt.plot(times, low_2019, label = "하")
plt.legend()
plt.show()
