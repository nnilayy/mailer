# demo.py
from email_sender import send_email_with_attachments

# Define the email details
to_email = 'nnilayy.work@gmail.com'  # Replace with the recipient's email address
subject = 'Test Email with Attachments and Tracking Pixel'
body = '''
Hello,

This is a test email sent from a demo script. Please find the attachments and note that this email contains a tracking pixel.

Best regards,
Your Name
'''

# Define attachment URLs (use URLs to accessible files or None if not needed)
resume_url = 'https://drive.google.com/file/d/1mggvGbZYUdiZGnU3JUnIyRICjwElL0nB/view?pli=1'  # Replace with your actual resume link
cover_letter_url = 'https://drive.google.com/file/d/1mggvGbZYUdiZGnU3JUnIyRICjwElL0nB/view?pli=1'  # Replace with your actual cover letter link

# Send the email
try:
    send_email_with_attachments(to_email, subject, body, resume_url, cover_letter_url)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
