# data_handler.py
import sqlite3
from datetime import datetime

DB_FILE = 'emails.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT,
            name TEXT,
            role TEXT,
            address TEXT,
            email TEXT,
            subject TEXT,
            body TEXT,
            scheduled_date TEXT,
            resume_link TEXT,
            cover_letter_link TEXT,
            status TEXT DEFAULT 'Pending',
            opened TEXT DEFAULT '',
            open_time TEXT DEFAULT '',
            open_count INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def get_pending_emails():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emails WHERE status = 'Pending'")
    rows = cursor.fetchall()
    conn.close()

    emails = []
    for row in rows:
        emails.append({
            'id': row[0],
            'company': row[1],
            'name': row[2],
            'role': row[3],
            'address': row[4],
            'email': row[5],
            'subject': row[6],
            'body': row[7],
            'scheduled_date': row[8],
            'resume_link': row[9],
            'cover_letter_link': row[10],
            'status': row[11],
            'opened': row[12],
            'open_time': row[13],
            'open_count': row[14]
        })
    return emails

def update_email_status(email_id, status):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE emails SET status = ? WHERE id = ?", (status, email_id))
    conn.commit()
    conn.close()

def update_email_open(email):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, open_count FROM emails WHERE email = ?", (email,))
    result = cursor.fetchone()
    if result:
        email_id, open_count = result
        open_count = open_count + 1
        open_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("UPDATE emails SET opened = 'Yes', open_time = ?, open_count = ? WHERE id = ?",
                       (open_time, open_count, email_id))
        conn.commit()
    conn.close()

def insert_email_record(form_data):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO emails (company, name, role, address, email, subject, body, scheduled_date, resume_link, cover_letter_link)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        form_data['company'],
        form_data['name'],
        form_data['role'],
        form_data['address'],
        form_data['email'],
        form_data['subject'],
        form_data['body'],
        form_data['scheduled_date'],
        form_data['resume_link'],
        form_data['cover_letter_link']
    ))
    conn.commit()
    conn.close()
