import csv
import matplotlib.pyplot as plt

f = open("person.csv",encoding = "euc - kr")
data = csv.reader(f)
next(data)

area = input('구 단위로 검색:')

name = []
tot = []

for row in data :
    row[1:] = map(int,row[1:])
    sumB = 0
    sumG = 0
    if area in row[0]:
        for i in range(17,23) :
            sumB += row[i]
            sumG += row[i + 63]
        name.append(row[0][:-12])
        tot.append(sumB + sumG)
print(name)
print(tot)

f.close()

del name [0]
del tot [0]

plt.rc("font",family ="Malgun Gothic")
plt.title("%s 청소년 인구 수" % area)

plt.barh(name,tot,color = "green")
plt.show()

f.close()
