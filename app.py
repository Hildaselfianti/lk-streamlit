import streamlit as st
import matplotlib.pyplot as plt

#Menambahkan judul
st.title("Welcome to Selpy's")

#menambahkan header
st.header('Introducing')
st.write('Halo! Nama saya Selpy. Saya adalah mahasiswi bisnis digital, sedang belajar membuat aplikasi web dengan Python. Dalam aplikasi pertama ini, saya memegang peran sebagai pengelola sebuah usaha di bidang kuliner yang sedang berkembang. Nanti saya akan memperlihatkan daftar tim kerja yang saya ciptakan sebagai simulasi. Semoga kalian menikmati aplikasi ini!!')
         
#Menambahkan subheader (tulisannya lebih kecil dari header)
st.subheader('The Data')

#Menambahkan caption (tulisan kecil yang tidak terlalu mencolok)
st.caption('Sesuai yang saya tulis di atas bahwa data ini tidak real.')

#Mendemonstrasikan kode
st.code('import streamlit as st')
st.text('Ini adalah teks penting yang harus di ketik untuk mendapatkan tampilan seperti yang tertera di layar anda.')

#Menampilkan rumus
st.latex(r' y = mx + b ')
st.text("Code yang dipakai untuk menampilkan rumus seperti di atas adalah (r' y = mx + b ')")

#Mengubah tebal, miring, gambar, tautan, and other
st.markdown('**Link** dan _link_ serta [Tautan](https://streamlit.io)')

#membuat garis horizontal untuk memisahkan materi atau apapun itu
st.divider()

import streamlit as st
import requests
import pandas as pd

data = {
    'Nama': ['Selpy', 'Naya', 'Hera'],
    'Hobi': ['Jalan-Jalan', 'Belanja', 'Membaca'],
    'Jurusan': ['Bisnis Digital', 'Pendidikan Ekonomi', 'Pendidikan Ekonomi']
}

df = pd.DataFrame(data)

# Daftar tim kerja simulasi
team = [
    {"Nama": "Andi", "Peran": "Kepala Koki", "Kontak": "andi@email.com"},
    {"Nama": "Sari", "Peran": "Asisten Koki", "Kontak": "sari@email.com"},
    {"Nama": "Budi", "Peran": "Manajer Operasional", "Kontak": "budi@email.com"},
    {"Nama": "Rina", "Peran": "Petugas Kasir", "Kontak": "rina@email.com"},
    {"Nama": "Dewi", "Peran": "Pelayan", "Kontak": "dewi@email.com"},
]

st.subheader('Daftar Tim Kerja Simulasi')
st.table(team)

# Daftar penjualan simulasi
sales = [
    {"No": 1, "Produk": "Nasi Goreng", "Jumlah": 20, "Harga Satuan (Rp)": 15000, "Total (Rp)": 20*15000},
    {"No": 2, "Produk": "Mie Ayam", "Jumlah": 15, "Harga Satuan (Rp)": 12000, "Total (Rp)": 15*12000},
    {"No": 3, "Produk": "Sate Ayam", "Jumlah": 10, "Harga Satuan (Rp)": 20000, "Total (Rp)": 10*20000},
    {"No": 4, "Produk": "Es Teh Manis", "Jumlah": 25, "Harga Satuan (Rp)": 5000, "Total (Rp)": 25*5000},
    {"No": 5, "Produk": "Jus Jeruk", "Jumlah": 18, "Harga Satuan (Rp)": 8000, "Total (Rp)": 18*8000},
]

st.subheader('Daftar Penjualan Simulasi')
st.table(sales)
col1, col2 = st.columns(2)
st.divider()

#Menampilkan grafik
import numpy as np
import streamlit as st

#Line Chart
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(data)

#Bar Chart
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

st.bar_chart(data)

#altair chart
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

chart = alt.Chart(data.reset_index()).mark_line().encode(
    x='index',
    y='a'
)

st.altair_chart(chart, use_container_width=True)

{"Nama": "Budi", "Peran": "Manajer Operasional", "Kontak": "budi@email.com"},
{"Nama": "Rina", "Peran": "Petugas Kasir", "Kontak": "rina@email.com"},
{"Nama": "Dewi", "Peran": "Pelayan", "Kontak": "dewi@email.com"},

st.subheader("Daftar Tim Kerja Simulasi")
st.table(team)
st.markdown("---")
st.header("Input Data Penjualan Kuliner")
with st.form("form_penjualan"):
    produk = st.text_input("Nama Produk")
    jumlah = st.number_input("Jumlah Terjual", min_value=0, step=1)
    harga_satuan = st.number_input("Harga Satuan (Rp)", min_value=0, step=1000)
    tanggal = st.date_input("Tanggal Penjualan")
    submitted = st.form_submit_button("Simpan Data Penjualan")

if submitted:
    total = jumlah * harga_satuan
    st.success(f"Data penjualan produk {produk} berhasil disimpan!")
    st.write(f"Jumlah Terjual: {jumlah}")
    st.write(f"Harga Satuan: Rp{harga_satuan:,}")
    st.write(f"Total Pendapatan: Rp{total:,}")
    st.write(f"Tanggal Penjualan: {tanggal}")

    #Menampilkan Gambar
import streamlit as st
from PIL import Image

st.image(
    "https://wonderfulselayar.id/wp-content/uploads/2022/07/DJI_0206-28-scaled.jpg",
    caption="Saya tinggal di selayar",
    use_container_width=True
)

caption="Saya berasal dari selayar",
use_container_width=True

#Menampilkan video dari file lokal
st.video('Hilda Selfianti.mp4')






