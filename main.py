from fastapi import FastAPI
from google.oauth2 import service_account
from google.auth import jwt
import datetime
import json
import os

app = FastAPI()

@app.get("/get-jwt")
def generate_jwt():
    # Charger la clé de service depuis variable d'environnement
    sa_key = json.loads(os.environ['GOOGLE_SERVICE_KEY'])

    now = datetime.datetime.utcnow()
    expiry = now + datetime.timedelta(hours=1)

    payload = {
        "iss": sa_key["client_email"],
        "scope": "https://www.googleapis.com/auth/cloud-platform",
        "aud": sa_key["token_uri"],
        "iat": int(now.timestamp()),
        "exp": int(expiry.timestamp())
    }

    signed_jwt = jwt.encode(sa_key, payload)
    return { "jwt": signed_jwt.decode("utf-8") }
