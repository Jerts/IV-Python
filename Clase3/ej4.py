import numpy as np

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1],[2],[3]]
#C = [[0],[0],[0]]



m = len(A)
l = len(A[0])
n = len(B[0])

# C = []
# for _ in range(m):
#     lista_temporal = []
#     for _ in range(n):
#         lista_temporal.append(0)
#     C.append(lista_temporal)
# print(C)

C = [ [ 0 for _ in range(n)] for _ in range(m)]
print(C)

for i in range(m):
    for j in range(n):
        suma=0
        for k in range(l):
            suma = suma + A[i][k]*B[k][j]
        C[i][j]=suma
print(C)

array_a_numpy = np.asarray(A,dtype = float)
array_b_numpy = np.asarray(B,dtype = float)
D = np.dot(array_a_numpy,array_b_numpy)
print(D)