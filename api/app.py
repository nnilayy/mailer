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

    # 1x1 transparent GIF
    transparent_gif = (
        b'GIF89a'
        b'\x01\x00\x01\x00'
        b'\x80\x00\x00'
        b'\x00\x00\x00'
        b'\x00\x00\x00'
        b'\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02'
        b'\x44\x01\x00\x3b'
    )

    # Add cache-busting headers
    headers = {
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "Pragma": "no-cache",
        "Expires": "0",
        "Content-Type": "image/gif"
    }

    return Response(content=transparent_gif, headers=headers)
