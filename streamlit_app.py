import streamlit as st

st.title("-bgshad")
st.write("💲🎰 bukan adiksi tapi dedikasi🤑😈🙏🏿.")
st.image("05_39_10_Gdillk_WMAAtPqx.jpg", width=200)

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")
