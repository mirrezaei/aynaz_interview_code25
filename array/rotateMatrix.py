
def rotate(x):
  #x [[],[]] n*n
  rotatedX=[]
  for j in range(len(x)): # 0 to n -> columns
    row=[]
    for i in range(len(x)-1,-1,-1):# n-1 to 0 -> rows
      row.append(x[i][j])
    rotatedX.append(row)

  return rotatedX


def rotateInPlace(x):
    l=len(x)
    i=l
    while(i>=0):
        



x=[[1,2],[3,4]]
print(rotate(x))