import csv

f =open("accident.csv",encoding = "cp949")
data = csv.reader(f)

next(data)
i = 0
road_type = []
number = []

for row in data :
    row[2:] = map(int,row[2:])
    if i< 49:
        if i % 7 == 5:
            road_type.append(row[0])
            number.append(row[2])

        i += 1

for i in range(len(road_type)):
    print(road_type[i],':',number[i])

f.close()
