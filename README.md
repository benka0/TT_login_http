Minimal insecure login demo (for classroom sniffing exercise)

Files:
- app.py
- templates/login.html
- requirements.txt
- Dockerfile
- openshift.yaml

Run locally (Windows):
1. python -m venv venv
2. venv\Scripts\activate
3. pip install -r requirements.txt
4. python app.py
5. Browse to http://<server-ip>:8000

Rahti import (recommended): push this repo and use "Import from Git" in Rahti web console.

Security: Use an isolated lab network and test accounts only. Do NOT expose to public internet.
