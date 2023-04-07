import streamlit as st
import qrcode
from io import BytesIO

st.title('App para gerar QR Code')

texto = st.text_input('Digite o texto para gerar o QR Code:')

if texto:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(texto)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    
    # Converter a imagem para bytes
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()
    
    st.image(img_bytes, caption='QR Code gerado')

