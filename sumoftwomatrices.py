mat1,mat2,mat3=[],[],[]
row=int(input("no of rows: "))
col=int(input("no of col: "))
for i in range(1,row+1):
    a=[]
    for j in range(1,col+1):
        print("Enter value for", i, "row and", j, "column of first matrix")
        k=int(input())
        a.append(k)
    mat1.append(a)
for i in range(1,row+1):
    b=[]
    for j in range(1,col+1):
        print("Enter value for", i, "row and", j, "column of second matrix")
        k=int(input())
        b.append(k)
    mat2.append(b)
for i in range(row):
    c=[]
    for j in range(col):
        c.append(mat1[i][j]+mat2[i][j])
    mat3.append(c)
    print()
for i in range(row):
    for j in range(col):
        print(mat1[i][j],end=" ")
    print()
print()
for i in range(row):
    for j in range(col):
        print(mat2[i][j],end=" ")
    print()
print()
for i in range(row):
    for j in range(col):
        print(mat3[i][j],end=" ")
    print()