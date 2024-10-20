from databricks import sql

def get_data_from_databricks():
    connection = sql.connect(
        server_hostname="adb-3222227712665162.2.azuredatabricks.net",
        http_path="/sql/1.0/warehouses/c938a39859d227a8",
        access_token="dapi7652ad8e5e7597f420c5769a8d88a0f5-3"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM eq_sracpper.default.combined_news")
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    columns = ['Headline', 'URL', 'Source', 'Datetime']
    return [dict(zip(columns, row)) for row in data]
