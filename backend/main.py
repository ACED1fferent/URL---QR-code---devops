from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydantic import BaseModel
import qrcode
from io import BytesIO

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://backend:8000/qr",
    "http://localhost:3000/favicon.ico",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UrlRequest(BaseModel):
    url: str

@app.get("/ping")
def ping():
    return {"msg": "ok"}


@app.post("/qr")
def generate_qr(data: UrlRequest):
    if not data.url:
        raise HTTPException(status_code=400, detail="URL is required")

    img = qrcode.make(data.url)
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    return Response(content=buf.getvalue(), media_type="image/png")
