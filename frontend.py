import streamlit as st
import requests

st.title("Background Remover")

file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if file:
    st.image(file, caption="Original Image")
    
    if st.button("Remove Background"):
        # The spinner will show up here
        with st.spinner("Processing... please wait"):
            try:
                # Send to FastAPI
                res = requests.post("http://localhost:8000/process", files={"file": file})
                # res = requests.post("/process", files={"file": file})
                
                # Show Result
                if res.status_code == 200:
                    st.image(res.content, caption="Background Removed!")
                else:
                    st.error("Backend error. Check your FastAPI terminal.")
            except Exception as e:
                st.error(f"Connection failed. Is the backend running? Error: {e}")