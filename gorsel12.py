import streamlit as st
import requests
import io
import base64
import os
from PIL import Image
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()
STABILITY_KEY = os.environ.get("STABILITY_API_KEY")
ENGINE_ID = "stable-diffusion-xl-1024-v1-0"
BASE_URL = f"https://api.stability.ai/v1/generation/{ENGINE_ID}"

# API Helper Fonksiyonu
def process_api_call(endpoint, files=None, data=None, json=None):
    headers = {"Authorization": f"Bearer {STABILITY_KEY}"}
    response = requests.post(
        f"{BASE_URL}/{endpoint}",
        headers=headers,
        files=files,
        data=data,
        json=json
    )
    if response.status_code != 200:
        raise Exception(f"API Hatası: {response.text}")
    return response.json()["artifacts"][0]["base64"]

# Görsel Oluşturma Fonksiyonları
def generate_image(prompt, height=1024, width=1024):
    return process_api_call(
        "text-to-image",
        json={
            "text_prompts": [{"text": prompt}],
            "cfg_scale": 7,
            "height": height,
            "width": width,
            "steps": 30
        }
    )

def create_variation(image_file, prompt=None):
    files = {"init_image": image_file}
    data = {
        "image_strength": 0.35,
        "text_prompts[0][text]": prompt or "Create a variation",
        "cfg_scale": 7,
        "steps": 30
    }
    return process_api_call("image-to-image", files=files, data=data)

def inpainting(image_file, mask_file, prompt):
    files = {
        "init_image": image_file,
        "mask_image": mask_file
    }
    data = {
        "text_prompts[0][text]": prompt,
        "cfg_scale": 7,
        "steps": 30
    }
    return process_api_call("image-to-image/masking", files=files, data=data)

def outpainting(image_file, prompt, expand_ratio=0.25):
    files = {"init_image": image_file}
    data = {
        "text_prompts[0][text]": prompt,
        "cfg_scale": 7,
        "steps": 30,
        "expand_ratio": expand_ratio
    }
    return process_api_call("image-to-image/outpainting", files=files, data=data)

# Streamlit Arayüzü
st.set_page_config(layout="wide", page_title="AI Görsel İşleme Merkezi")
st.title("🖼️ AI Görsel İşleme Merkezi")

with st.sidebar:
    st.header("Ayarlar")
    st.info("Stability AI API v1.0 | Gelişmiş Görsel İşleme")

# Metinden Görsel Oluşturma
with st.expander("✨ Metinden Görsel Oluştur", expanded=True):
    col1, col2 = st.columns(2)
    width = col1.number_input("Genişlik", 512, 2048, 1024)
    height = col2.number_input("Yükseklik", 512, 2048, 1024)
    prompt = st.text_input("Görsel açıklaması:")
    
    if st.button("Oluştur"):
        with st.spinner("AI görsel üretiyor..."):
            try:
                image_data = generate_image(prompt, height, width)
                img = Image.open(io.BytesIO(base64.b64decode(image_data)))
                st.image(img, caption=prompt, use_column_width=True)
            except Exception as e:
                st.error(f"Hata: {str(e)}")

# Görsel Varyasyonu
with st.expander("🔄 Görsel Varyasyonu"):
    col_upload, col_result = st.columns(2)
    with col_upload:
        uploaded_file = st.file_uploader("Temel görsel seçin", type=["png", "jpg", "jpeg"])
        if uploaded_file:
            st.image(uploaded_file, caption="Yüklenen Görsel", use_column_width=True)
    
    with col_result:
        variation_prompt = st.text_input("Varyasyon için açıklama:")
        if st.button("Varyasyon Oluştur") and uploaded_file:
            with st.spinner("Varyasyon oluşturuluyor..."):
                try:
                    img_byte_arr = io.BytesIO()
                    Image.open(uploaded_file).save(img_byte_arr, format='PNG')
                    img_byte_arr.seek(0)
                    
                    variation_data = create_variation(img_byte_arr, variation_prompt)
                    variation_img = Image.open(io.BytesIO(base64.b64decode(variation_data)))
                    st.image(variation_img, caption="Oluşturulan Varyasyon", use_column_width=True)
                except Exception as e:
                    st.error(f"Hata: {str(e)}")


st.markdown("---")
st.caption("© 2024 AI Görsel İşleme Merkezi | Stability AI API Entegrasyonu")