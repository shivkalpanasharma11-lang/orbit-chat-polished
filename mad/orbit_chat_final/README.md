# Orbit Chat — Final Layout Fix

This edition keeps the animated plum / rose / lime visual design, but fixes the overly large message composer. The conversation is centered at a moderate width, and the input is constrained to a maximum of 820px with an approximately 58px height on desktop.

## Run locally on Windows / VS Code
Open this folder in VS Code, then run these commands one at a time:

```powershell
py -m pip install -r requirements.txt
py -m streamlit run app.py
```

## Replace the deployed version
Upload this `app.py` to your existing GitHub repository, replace the old file, and commit the change. Wait for Streamlit Community Cloud to redeploy and refresh your existing link.

## Capability note
This is a no-API demo that matches questions to a curated knowledge library. It is not a live generative AI model.
