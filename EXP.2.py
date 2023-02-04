X=[[1,2,3],
   [4,5,6]]

Y=[[6,5,4],
   [3,2,1]]
result = [[X[i][j]+Y[i][j] for j in range(len(X[0]))]for i in range(len(X))]
for r in result:
    print(r)
