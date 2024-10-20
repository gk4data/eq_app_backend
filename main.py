from fastapi import FastAPI
from db_config import get_data_from_databricks

app = FastAPI()

@app.get("/api/news")
def fetch_news():
    data = get_data_from_databricks()
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
