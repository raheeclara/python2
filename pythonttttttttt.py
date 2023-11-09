import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
plt.rc("font", family = "Malgun Gothic")

df = pd.read_html("https://ko.wikipedia.org/wiki/%EA%B8%B0%EB%8C%80%EC%88%98%EB%AA%85%EC%88%9C_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D")[0]
'''
print(df.sort_values(by = "남성", ascending = False).head(5))
print(df.sort_values(by = "여성", ascending = False).head(5))
'''
'''
df_m_avg = df["남성"].mean()
df_w_avg = df["여성"].mean()

print("Men :", df_m_avg)
print("Women :",df_w_avg)

difference = abs(df_m_avg - df_w_avg)

if  df_m_avg > df_w_avg :
    gender1, gender2 = "men","women"
else :
    gender1, gender2 = "women", "men"

print("On anverage, %s live %.2f years longer than %s." % (gender1, difference, gender2))
 '''
'''
gender = ["남자","여자"]
gender_list =[]
height_list = []
weight_list = []

for i in range(100):
    idx = np.random.randint(2)
    gender_list.append(gender[idx])
    if idx == 0 :
        height_list.append(np.random.randint(170, 190))
        weight_list.append(np.random.randint(70, 80))
    else :
        height_list.append(np.random.randint(150, 165))
        weight_list.append(np.random.randint(40, 60))
data2 = {"gender" : gender_list, "height" : height_list, "weight" : weight_list}

ex_df2 = pd.DataFrame(data2)

sns.scatterplot(data = ex_df2, x = "weight", y = "height", hue = "gender")
plt.show()
'''

sns.scatterplot(x = "남성", y = "여성", data = df)
plt.xlim(45, 90)
plt.ylim(45, 90)
plt.plot([45, 90], [45,90], 'r')
plt.tight_layout()
plt.grid()
plt.show()


















