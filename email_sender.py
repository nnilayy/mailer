# email_sender.py
import smtplib
import ssl
from email.message import EmailMessage
import requests
from config import SMTP_SERVER, SMTP_PORT, MY_EMAIL, MY_PASSWORD, VERCEL_APP_URL
from utils import get_direct_download_link

def send_email_with_attachments(to_email, subject, body, resume_url=None, cover_letter_url=None):
    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = MY_EMAIL
    msg['To'] = to_email
    msg.set_content(body, subtype='html')

    # Embed tracking pixel
    tracking_pixel_url = f'{VERCEL_APP_URL}/api/track?email={to_email}'
    tracking_pixel = f'<img src="{tracking_pixel_url}" width="1" height="1" style="display:none;">'
    msg.add_alternative(f'{body}{tracking_pixel}', subtype='html')

    # Attach Resume
    attachments = []
    if resume_url:
        direct_resume_url = get_direct_download_link(resume_url)
        resume_content = requests.get(direct_resume_url).content
        msg.add_attachment(resume_content, maintype='application', subtype='pdf', filename='Resume.pdf')

    # Attach Cover Letter
    if cover_letter_url:
        direct_cover_letter_url = get_direct_download_link(cover_letter_url)
        cover_letter_content = requests.get(direct_cover_letter_url).content
        msg.add_attachment(cover_letter_content, maintype='application', subtype='pdf', filename='CoverLetter.pdf')

    # Send the email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.login(MY_EMAIL, MY_PASSWORD)
        server.send_message(msg)
