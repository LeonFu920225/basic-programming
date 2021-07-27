sc = [[1, 'A', 80, 95, 88, 0, 0, 0],
      [2, 'B', 98, 97, 96, 0, 0, 0],
      [3, 'C', 91, 93, 95, 0, 0, 0],
      [4, 'D', 92, 94, 90, 0, 0, 0],
      [5, 'E', 92, 97, 90, 0, 0, 0],
     ]
print("原始成績單->")
for i in range(len(sc)):
    print(sc[i])
for i in range(len(sc)):
    sc[i][5] = sum(sc[i][2:5])
    sc[i][6] = round((sc[i][5])/3,2)
sc.sort(key=lambda x:x[5],reverse = True)
for i in range(len(sc)):
    if sc[i][6] == sc[i-1][6]:
        sc[i][7] = i
    else:
        sc[i][7] = i + 1
sc.sort(key=lambda x: x[0])
print("最後成績單->")
for i in range(len(sc)):
    print(sc[i])