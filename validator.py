from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import re
import dns.resolver
from typing import Dict

app = FastAPI()

# Allow CORS from your frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change * to your React domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Expanded list of disposable email domains
DISPOSABLE_DOMAINS = [
    "mailinator.com", "10minutemail.com", "tempmail.com", "guerrillamail.com",
    "trashmail.com", "yopmail.com", "fakeinbox.com", "dispostable.com",
    "maildrop.cc", "emailondeck.com", "moakt.com", "getairmail.com",
    "mytemp.email", "throwawaymail.com", "sharklasers.com", "spamgourmet.com",
    "mintemail.com", "spambog.com", "mailnesia.com"
]

def is_valid_email_format(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def has_mx_record(domain: str) -> bool:
    try:
        dns.resolver.resolve(domain, 'MX')
        return True
    except:
        return False

def is_disposable_email(domain: str) -> bool:
    return domain.lower() in DISPOSABLE_DOMAINS

@app.get("/validate")
def validate_email_basic(email: str = Query(..., description="Email address to validate")) -> Dict:
    domain = email.split("@")[-1]
    return {
        "email": email,
        "is_valid_format": is_valid_email_format(email),
        "has_mx_records": has_mx_record(domain),
        "is_disposable": is_disposable_email(domain),
    }
