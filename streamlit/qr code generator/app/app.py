import streamlit as st
import qrcode
from PIL import Image

st.set_page_config(page_title="QR Code Generator", layout="centered")

st.title("🔗 QR Code Generator")

link = st.text_input("Enter link:")
filename = st.text_input("Enter filename (with .png):", "qrcode.png")

if st.button("Generate QR Code"):
    if link.strip() == "":
        st.warning("Please enter a valid link.")
    else:
        qr = qrcode.QRCode(box_size=10, border=4)
        qr.add_data(link.strip())
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        img.save(filename)

        st.success(f"QR Code saved as {filename}")
        st.image(Image.open(filename), caption="Generated QR Code")
