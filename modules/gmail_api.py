from __future__ import print_function
import base64 
import os
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# gmail api scope
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_gmail_services():
    """
    Autenticate and return a gmail service instance. Returns service, an authorization api service instance
    """

    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json',SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json',SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json','w') as token:
            token.write(creds.to_json())
    service = build('gmail','v1',credentials=creds)
    return service

def create_message(sender: str,to: str,subject: str, message_text) -> dict:
    """
    create message email. args: sender: email of the sender, to, email to recieve,subject:email subject,message_text body of email
    returns a dictionary object ready to be sent
    """
    message = MIMEText(message_text)
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw':raw}

def send_message(service,user_id:str,message:dict) -> dict:
    """Sends an email. args: service: gmail api service instance, instance,user_id. your id, message: message object created using create message()
    Return a dict with sent message metadata
    """
    sent = service.users().messages().send(userId=user_id,body=message).execute()
    print(f"Message id:{sent['id']}")
    return sent