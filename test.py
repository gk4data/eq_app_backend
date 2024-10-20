import requests
import pandas as pd

# Fetch data from your FastAPI endpoint
response = requests.get("http://127.0.0.1:8000/api/news")

# Convert the JSON data to a pandas DataFrame
if response.status_code == 200:
    data = response.json()  # Get the JSON data
    df = pd.DataFrame(data)  # Convert it to a pandas DataFrame
    print(df)  # Display the DataFrame
else:
    print(f"Error: {response.status_code}")




