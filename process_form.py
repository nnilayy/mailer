# process_form.py
from api.data_handler import insert_email_record

form_data = {
    'company': 'Example Corp',
    'name': 'John Doe',
    'role': 'Software Engineer',
    'address': '123 Main St',
    'email': 'recipient@example.com',
    'subject': 'Job Application',
    'body': 'Dear Hiring Manager,\n\nPlease find attached my resume and cover letter.\n\nBest regards,\nJohn Doe',
    'scheduled_date': '2023-10-01 09:00:00',
    'resume_link': 'https://drive.google.com/file/d/your_resume_id/view?usp=sharing',
    'cover_letter_link': 'https://drive.google.com/file/d/your_cover_letter_id/view?usp=sharing'
}

# insert_email_record(form_data)
print("Form data processed and email scheduled.")
