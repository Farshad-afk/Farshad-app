import streamlit as st

st.title("-bgshad")
st.write("💲🎰 bukan adiksi tapi dedikasi🤑😈🙏🏿.")
st.image("05_39_10_Gdillk_WMAAtPqx.jpg", width=300)

st.title("Gacor 777🎰")
st.header("Mengecek Angka")
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
  st.write(f" {angka} Rugi kau niga🙏🏿😈")
else:
  st.write(f"{angka} Kau Jackpot 🤑💰💲🎰")
