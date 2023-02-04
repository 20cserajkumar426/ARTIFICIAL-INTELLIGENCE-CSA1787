x=[[1,3],
   [4,5],
   [7,8]]

transpose=[[1,4,7],[3,5,8]]
for i in range(len(x)):
    for j in range(len(x[0])):
               transpose[j][i]=x[i][j]
for t in transpose:
    print(t)
