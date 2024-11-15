from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Enable CORS for all origins, methods, and headers for maximum compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; adjust this if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/track")
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
