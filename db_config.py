# db_config.py
import pyodbc
import os


def get_connection():
    # Get environment variables (or hard-code the values if you prefer)
    server = os.getenv('DB_SERVER', 'eq-news.database.windows.net')
    database = os.getenv('DB_NAME', 'backend_eq_news')
    username = os.getenv('DB_USER', 'eq_news_db')
    password = os.getenv('DB_PASSWORD', 'Ganesh@139')
    driver = '{SQL Server}'
    
    # Establish a connection to the Azure SQL database
    connection = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    )
    return connection
