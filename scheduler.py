# scheduler.py
import schedule
import time
from api.data_handler import get_pending_emails, update_email_status
from email_sender import send_email_with_attachments
from datetime import datetime

def job():
    pending_emails = get_pending_emails()
    for email_data in pending_emails:
        # Check if the scheduled date/time has arrived
        scheduled_datetime = datetime.strptime(email_data['scheduled_date'], '%Y-%m-%d %H:%M:%S')
        if datetime.now() >= scheduled_datetime:
            try:
                send_email_with_attachments(
                    to_email=email_data['email'],
                    subject=email_data['subject'],
                    body=email_data['body'],
                    resume_url=email_data.get('resume_link'),
                    cover_letter_url=email_data.get('cover_letter_link')
                )
                update_email_status(email_data['id'], status='Sent')
                print(f"Email sent to {email_data['email']}")
            except Exception as e:
                print(f"Failed to send email to {email_data['email']}: {e}")

def schedule_emails():
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
