from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydantic import BaseModel
import qrcode
from io import BytesIO
import httpx

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:30081",
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

# Health check endpoint
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

# Proxy endpoint that the browser can call in Minikube
@app.post("/proxy/qr")
async def proxy_qr(data: UrlRequest):
    async with httpx.AsyncClient() as client:
        resp = await client.post("http://qr-backend:8000/qr", json={"url": data.url})
    return Response(content=resp.content, media_type="image/png")
