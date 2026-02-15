# uvicorn streamlit_app:app --reload

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Background Remover API is running"}

@app.post("/process")
async def process(file: UploadFile = File(...)):
    data = await file.read()
    output = remove(data)
    return Response(content=output, media_type="image/png")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8501)