from fastapi import FastAPI
from supabase import create_client, Client
import os

app = FastAPI()

# Render environment variables se keys read karega
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "Custom Cricket API is live and connected!"}

@app.get("/api/v1/matches")
def get_matches():
    try:
        response = supabase.table("Matches").select("*").execute()
        return {"status": "success", "data": response.data}
    except Exception as e:
        return {"status": "error", "message": str(e)}
        
