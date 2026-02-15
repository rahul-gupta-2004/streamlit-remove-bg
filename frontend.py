import streamlit as st
import requests

# api_url = "http://localhost:8000/process"
# Replace with your actual API URL
api_url = "https://bg-remover-api.streamlit.app/process"

st.title("Background Remover")

file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if file:
    st.image(file, caption="Original Image")
    
    if st.button("Remove Background"):
        with st.spinner("Processing... please wait"):
            try:
                res = requests.post(url=api_url, files={"file": file})
                
                if res.status_code == 200:
                    st.image(res.content, caption="Background Removed!")
                else:
                    st.error("Backend error. Check your API logs.")
            except Exception as e:
                st.error(f"Connection failed. Error: {e}")