from fastapi import FastAPI
from supabase import create_client, Client
import os

app = FastAPI()

# Supabase Credentials
SUPABASE_URL = "https://pgvbntkzmevwrgzduxvu.supabase.co"
SUPABASE_KEY = "sb_publishable_Fi0UIon1oVFJDFHbwukjBw_3fA662QL"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "Custom Cricket API is live and connected!"}

@app.get("/api/v1/matches")
def get_matches():
    try:
        # Matches table se data fetch karna
        response = supabase.table("Matches").select("*").execute()
        return {"status": "success", "data": response.data}
    except Exception as e:
        return {"status": "error", "message": str(e)}
      
