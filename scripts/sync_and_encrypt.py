import os
import sys
import json
import base64
import urllib.request
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def get_env_or_file(env_var, filepath=None):
    val = os.environ.get(env_var)
    if val:
        return val.strip()
    if filepath and os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read().strip()
    return None

def fetch_url(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) SmartDashboardSync/1.0'})
    with urllib.request.urlopen(req, timeout=15) as r:
        return r.read().decode('utf-8', errors='ignore')

import datetime

def main():
    personal_url = os.environ.get('PERSONAL_ICS_URL')
    family_url = os.environ.get('FAMILY_ICS_URL')
    secret_key_hex = get_env_or_file('CALENDAR_SECRET_KEY', '.master_key')

    if not secret_key_hex:
        print("ERROR: CALENDAR_SECRET_KEY not set.")
        sys.exit(1)

    feeds_data = []

    if personal_url:
        print("Fetching Personal calendar...")
        try:
            p_text = fetch_url(personal_url)
            if 'BEGIN:VCALENDAR' in p_text:
                feeds_data.append({
                    "name": "Personal",
                    "color": "sky",
                    "ics": p_text
                })
                print(f"  Personal: OK ({len(p_text)} bytes)")
            else:
                print("  Personal: VCALENDAR header missing!")
        except Exception as e:
            print(f"  Personal fetch failed: {e}")

    if family_url:
        print("Fetching Family calendar...")
        try:
            f_text = fetch_url(family_url)
            if 'BEGIN:VCALENDAR' in f_text:
                feeds_data.append({
                    "name": "Family",
                    "color": "violet",
                    "ics": f_text
                })
                print(f"  Family: OK ({len(f_text)} bytes)")
            else:
                print("  Family: VCALENDAR header missing!")
        except Exception as e:
            print(f"  Family fetch failed: {e}")

    if not feeds_data:
        print("ERROR: No calendar feeds fetched successfully.")
        sys.exit(1)

    bundle = {
        "updated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "feeds": feeds_data
    }

    plaintext = json.dumps(bundle).encode('utf-8')

    # Encrypt using AES-256-GCM
    key_bytes = bytes.fromhex(secret_key_hex)
    aesgcm = AESGCM(key_bytes)
    nonce = os.urandom(12) # 96-bit IV
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    encrypted_payload = {
        "iv": base64.b64encode(nonce).decode('utf-8'),
        "data": base64.b64encode(ciphertext).decode('utf-8')
    }

    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "calendar_data.enc")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(encrypted_payload, f)

    print(f"\nEncrypted payload successfully generated at: {output_path}")
    print(f"Encrypted size: {len(encrypted_payload['data'])} base64 chars")

if __name__ == '__main__':
    main()
