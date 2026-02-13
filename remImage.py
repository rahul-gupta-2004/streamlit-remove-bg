# requirements: pip install fastapi streamlit rembg uvicorn python-multipart
# uvicorn remImage:app --reload

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove

app = FastAPI()

@app.post("/process")
async def process(file: UploadFile = File(...)):
    # 1. Get the image data
    data = await file.read()
    # 2. Remove background
    output = remove(data)
    # 3. Send it back
    return Response(content=output, media_type="image/png")