import streamlit as st 
import numpy as np 
import pandas as pd 
import random
import matplotlib.pyplot as plt

st.title("Fasta Method Program 🧬")
st.sidebar.title("Input Parameter and Sequence Here ✒️")
user_choose = st.sidebar.selectbox("Choose Input Mode", ["Default Example", "Random Generator System", "Input Manual"])

if user_choose == "Default Example":
    sequence_j = ["C", "C", "A", "T", "C", "G", "C", "C", "A", "T", "C", "G"]
    sequence_i = ["G", "C", "A", "T", "C", "G", "G", "C"]
elif user_choose == "Random Generator System":
    base = ["A", "G", "C", "T"]
    lenght_sequence_j = st.sidebar.number_input("Input Sequence J Lenght", value=12)
    lenght_sequence_i = st.sidebar.number_input("Input Sequence I Lenght", value=8)
    sequence_i = []
    sequence_j = []
    for i in range(lenght_sequence_j):
        sequence_j.append(base[random.randint(0,3)])
    for i in range (lenght_sequence_i):
        sequence_i.append(base[random.randint(0,3)])
elif user_choose == "Input Manual":
    input_user_j = st.sidebar.text_input("Input Sequence J", value=("ACTGTGACAGATAGG"))
    input_user_i = st.sidebar.text_input("Input Sequence J", value=("ACTGTGACAACCGG"))
    sequence_i = []
    sequence_j = []
    for base in range(len(input_user_j)):
        sequence_j.append(input_user_j[base])
    for base in range(len(input_user_i)):
        sequence_i.append(input_user_i[base])
k = st.sidebar.number_input("Input K Tuple", value=2)
if st.sidebar.button("start"):
    # Menggabungkan list menjadi satu string tanpa tampilan list
    sequence_j_str = ''.join(sequence_j)
    sequence_i_str = ''.join(sequence_i)

    # Menampilkan string kalimat
    st.write("Sequence J:", sequence_j_str)
    st.write("Sequence I:", sequence_i_str)
    
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
    st.subheader("Dot Matrix Represent the Fasta Alignment")
    # Tampilkan plot
    st.pyplot(plt)

    matrix_sequence_j = []
    matrix_sequence_i = []

    for i in range(len(sequence_j) - k + 1):
        temp = sequence_j[i:i + k]
        matrix_sequence_j.append(temp)

    for i in range(len(sequence_i) - k + 1):
        temp = sequence_i[i:i + k]
        matrix_sequence_i.append(temp)
    
    # Create a DataFrame for displaying the table
    data_sequence_j = {'Index': range(1, len(matrix_sequence_j)+1),
            'Base per K Tuple J': [''.join(t) for t in matrix_sequence_j]}
    df_j = pd.DataFrame(data_sequence_j)

    data_sequence_i = {'Index': range(1, len(matrix_sequence_i)+1),
        'Base per K Tuple I': [''.join(t) for t in matrix_sequence_i]}
    df_i = pd.DataFrame(data_sequence_i)
    st.subheader("k-word List Table for each Sequence")
    col1, col2 = st.columns(2)
    with col1: 
        st.write("k-word List Table for Sequence J")
        st.dataframe(df_j, use_container_width=True)
    with col2: 
        st.write("k-word List Table for Sequence I")
        st.dataframe(df_i, use_container_width=True)
    
    #Library to store matching sequence 
    n = len(sequence_i)  
    m = len(sequence_j)-1
    Sl_dict = {}

    for x in range(1 - m, n - 1):
        Sl = x # Kunci
        Sl_dict[Sl] = 0  

    for i in range (len(matrix_sequence_i)):
        for j in range (len(matrix_sequence_j)):
            if matrix_sequence_i[i] == matrix_sequence_j[j]:
                temp = (i + 1) - (j+1)
                print(f"{(i + 1)} - {(j+1)} = {temp}")
                key = temp
                if key in Sl_dict:
                    Sl_dict[key] += 1
    # Konversi kamus Sl_dict ke DataFrame
    df = pd.DataFrame(list(Sl_dict.items()), columns=['S', 'Sl'])
    # Transpose the DataFrame
    transposed_df = df.transpose()  # Using .transpose() method
    # OR
    transposed_df = df.T  # Using .T attribute
    st.subheader("Final Result for Scores of the Diagonals at Various Offsets")
    # Menampilkan DataFrame
    st.dataframe(transposed_df)
    



    
