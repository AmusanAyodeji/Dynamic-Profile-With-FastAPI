import requests
from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()

@app.get("/me")
def get_me():
    fact = "Error getting cat fact"
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        response.raise_for_status()
        data = response.json()
        fact = data.get("fact", fact)
    except (requests.Timeout, requests.RequestException, ValueError):
        pass
    return {
        "status": "success",
        "user":{
            "email":"ayobayonleamusan1@gmail.com",
            "name":"Ayodeji Amusan",
            "stack":"Python/FastAPI"
        },
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "fact": fact
    }