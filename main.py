# main.py
from fastapi import FastAPI, HTTPException
import pandas as pd
from db_config import get_connection

app = FastAPI()

# Fetch data from Azure SQL and return as a list of dicts (JSON response)
@app.get("/api/news")
def fetch_news():
    try:
        # Get the database connection
        conn = get_connection()
        query = "SELECT * FROM dbo.scrapped_news_data"
        
        # Load data into a pandas DataFrame
        df = pd.read_sql(query, conn)
        conn.close()
        
        # Convert the DataFrame to a list of dictionaries (JSON-like format)
        data = df.to_dict(orient='records')
        return {"data": data}
    
    except Exception as e:
        print(f"Error: {str(e)}")  # For debugging
        raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")
