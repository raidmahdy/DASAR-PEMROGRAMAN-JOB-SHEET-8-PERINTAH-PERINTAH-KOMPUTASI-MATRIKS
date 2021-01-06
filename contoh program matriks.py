import numpy as np 

print("PROGRAM MATRIKS")
B = int(input("Masukan jumlah baris:")) 
K = int(input("Masukan jumlah kolom:")) 
  
print("Masukan angka isi dari matriks dalam satu baris (pisahkan dengan spasi): ") 
  
# User input of entries in a  
# single line separated by space 
entri = list(map(int, input().split())) 
  
# For printing the matrix 
matrix = np.array(entri).reshape(B, K) 
print(matrix)
