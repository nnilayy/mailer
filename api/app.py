# api/track.py on Vercel
from fastapi import FastAPI, Request, Response
from datetime import datetime

app = FastAPI()

@app.get("/api/track")
async def track_email_open(request: Request):
    # Get the email query parameter
    email = request.query_params.get("email")
    
    # Log or save the tracking info
    # Here we're just printing it, but you could save to a database or file
    if email:
        print(f"Email opened by {email} at {datetime.now()}")

    # Return a 1x1 pixel transparent GIF
    transparent_gif = (
        b'GIF89a'           # Header
        b'\x01\x00\x01\x00' # Logical Screen Descriptor
        b'\x80\x00\x00'     # GCT follows for 1 entry
        b'\x00\x00\x00'     # Black color table entry
        b'\x00\x00\x00'     # Background color
        b'\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02'  # Image Descriptor
        b'\x44\x01\x00\x3b' # Image Data and Trailer
    )
    return Response(content=transparent_gif, media_type="image/gif")
