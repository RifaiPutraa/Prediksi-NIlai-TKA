import streamlit as st
import pandas as pd
import joblib

# konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Nilai TKA",
    page_icon="📘"
)

model = joblib.load("model.joblib")

st.title("📘 Prediksi Nilai TKA")
st.markdown("Aplikasi machine learning **regression** untuk memprediksi Nilai TKA siswa")

jam_belajar = st.slider("Jam Belajar per Hari", 0.0, 10.0, 4.0)
kehadiran = st.slider("Persen Kehadiran (%)", 0.0, 100.0, 80.0)
bimbel = st.pills("Mengikuti Bimbel?", ["ya", "tidak"], default="tidak")

if st.button("Prediksi Nilai TKA", type="primary"):
    data_baru = pd.DataFrame(
        [[jam_belajar, kehadiran, bimbel]],
        columns=["jam_belajar_per_hari", "persen_kehadiran", "bimbel"]
    )

    prediksi = model.predict(data_baru)[0]

    st.success(f"Model memprediksi **Nilai TKA ≈ {prediksi:.0f}**")
    st.balloons()

st.divider()
st.caption("Dibuat dengan 📘 oleh *RPL ❤*")