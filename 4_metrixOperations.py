import numpy as np
import numpy as pd

def input_matrix(name):
    print(f"\n enter element of matrix {name} (row wise) :")
    matrix =[]
    for i in range(3):
        row=list(map(int,input(f"row {i+1} (3 numbers seperated by spaces):").split()))
        matrix.append(row)
    return np.array(matrix)
A=input_matrix("A")
B=input_matrix("B")
scalar=int(input("\n enter scalar value:"))
print("\n addition:\n",A+B)
print("\n sub:\n",A-B)
print("\n mul:\n",np.dot(A,B))
print("\n scalar mul A by {scalar}:\n",A*scalar)
print("\n transpose:\n",A.T)
