# api/track.py
from fastapi import FastAPI, Response, Query
from starlette.responses import StreamingResponse
import datetime
import sys
import os

# Add the root directory of the project to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data_handler import update_email_open

app = FastAPI()

@app.get('/api/track')
async def track_email_open(email: str = Query(...)):
    # Record the email open event
    update_email_open(email)

    # Return a 1x1 transparent GIF
    transparent_gif_bytes = (
        b'GIF89a'           # Header
        b'\x01\x00\x01\x00' # Logical Screen Descriptor
        b'\x80\x00\x00'     # GCT follows for 1 entry
        b'\x00\x00\x00'     # Black color table entry
        b'\x00\x00\x00'     # Background color
        b'\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02'  # Image Descriptor
        b'\x44\x01\x00\x3b' # Image Data and Trailer
    )
    return Response(content=transparent_gif_bytes, media_type='image/gif')
