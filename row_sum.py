def rowsum(matrix,rows,columns):

    result=[]
    for i in range(rows):
        sum=0
        for j in range(columns):
            sum+=matrix[i][j]
        result.append(sum)
    return result

matrix=[]
rows=int(input("Enter number of rows : "))
columns=int(input("Enter number of columns : "))
for i in range(rows):
    matrix.append(list(map(int,input().split())))

print(rowsum(matrix,rows,columns))