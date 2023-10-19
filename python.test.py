import pandas as pd
import matplotlib.pyplot as plt

'''
data ={'name' : ['펭수','뽀로로','뿡뿡이','번개맨'],'age' : [10,5,10,20],'debut' : [2019,2003,2000,2000]}
df = pd.DataFrame(data)
print('1.',df.index)
print('2.',df.columns)
print('3.',df.values)
print(df.name)
'''

df = pd.read_html("https://ko.wikipedia.org/wiki/2020%EB%85%84_%EA%B0%80%EC%98%A8_%EB%94%94%EC%A7%80%ED%84%B8_%EC%B0%A8%ED%8A%B8_1%EC%9C%84_%EB%AA%A9%EB%A1%9D")
week = pd.DataFrame(df[0])
df_cnt = week.노래.value_counts()
plt.rc("font",family = "Malgun Gothic")
df_cnt.plot(x = week.노래 , y =df_cnt , kind = "bar")
plt.show()

'''
df = pd.DataFrame({"name" : ['펭수','뽀로로','뿡뿡이','번개맨'],'age' : [10,5,10,20]})

plt.rc("font",family = "Malgun Gothic")
df.plot(x = "name", y = "age", kind = "bar")
plt.show()
'''
