import streamlit as st 
import numpy as np 
import pandas as pd 
import random
import matplotlib.pyplot as plt

user_choose = st.sidebar.selectbox()

if user_choose == 1:
    sequence_j = ["C", "C", "A", "T", "C", "G", "C", "C", "A", "T", "C", "G"]
    sequence_i = ["G", "C", "A", "T", "C", "G", "G", "C"]
elif user_choose == 2:
    base = ["A", "G", "C", "T"]
    lenght_sequence_j = 12
    lenght_sequence_i = 8
    sequence_i = []
    sequence_j = []
    for i in range(lenght_sequence_j):
        sequence_j.append(base[random.randint(0,3)])
    for i in range (lenght_sequence_i):
        sequence_i.append(base[random.randint(0,3)])
elif user_choose == 3:
    input_user_j = str(input("Input sequence for J sequence:"))
    input_user_i = str(input("Input sequence for J sequence:"))
    sequence_i = []
    sequence_j = []
    for base in range(len(input_user_j)):
        sequence_j.append(input_user_j[base])
    for base in range(len(input_user_i)):
        sequence_i.append(input_user_i[base])


print(sequence_j)
print(sequence_i)
k = 2
labels_i = sequence_i
labels_j = sequence_j
# Inisialisasi matriks kesamaan dengan nol
matrix = [[0] * len(sequence_j) for _ in range(len(sequence_i))]

# Buat matriks kesamaan
for i in range(len(sequence_i)):
    for j in range(len(sequence_j)):
        subsequence_i = sequence_i[i:i + k]
        subsequence_j = sequence_j[j:j + k]
        if subsequence_i == subsequence_j:
            matrix[i][j] = k

# Tampilkan matriks kesamaan
for row in matrix:
    print(row)

# Gunakan fungsi imshow untuk menggambar matriks
plt.imshow(matrix, cmap='viridis')  # cmap adalah peta warna yang digunakan
# Tambahkan label untuk kolom (Sequence J)
plt.xticks(range(len(sequence_j)), sequence_j)
plt.xlabel("Sequence J")

# Tambahkan label untuk baris (Sequence I)
plt.yticks(range(len(sequence_i)), sequence_i)
plt.ylabel("Sequence I")

# Tambahkan bar warna
plt.colorbar()

# Tampilkan plot
plt.show()
