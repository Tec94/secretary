import requests
import msal
from load_keys import load_env
import os

load_env()

# Azure app registration details
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
tenant_id = os.getenv('tenant_id')

# Initialize the MSAL app
authority = f'https://login.microsoftonline.com/{tenant_id}'
app = msal.ConfidentialClientApplication(
    client_id,
    authority=authority,
    client_credential=client_secret,
)

# Acquire a token
scope = ["https://graph.microsoft.com/.default"]
result = app.acquire_token_for_client(scopes=scope)

if "access_token" in result:
    access_token = result["access_token"]
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }

    # Fetch emails
    endpoint = 'https://graph.microsoft.com/v1.0/users/<user-id>/messages'
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        emails = response.json()
        for email in emails['value']:
            print(f"Subject: {email['subject']}")
            print(f"From: {email['from']['emailAddress']['address']}")
            print(f"Received: {email['receivedDateTime']}")
            print(f"Body Preview: {email['bodyPreview']}\n")
    else:
        print(f"Error fetching emails: {response.status_code} {response.text}")
else:
    print(f"Error acquiring token: {result.get('error')}")
    print(result.get('error_description'))
    print(result.get('correlation_id'))
