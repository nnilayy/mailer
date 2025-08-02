from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from datetime import datetime

app = FastAPI()

# Enable CORS for all origins, methods, and headers for maximum compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return PlainTextResponse("Hello World")

@app.get("/api/greetuser")
async def track_email_open(request: Request):
    email = request.query_params.get("email")
    if email:
        print(f"Email opened by {email} at {datetime.now()}")

    transparent_gif = (
        b'GIF89a'
        b'\x01\x00\x01\x00'
        b'\x80\x00\x00'
        b'\x00\x00\x00'
        b'\x00\x00\x00'
        b'\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02'
        b'\x44\x01\x00\x3b'
    )
    return Response(content=transparent_gif, media_type="image/gif")
