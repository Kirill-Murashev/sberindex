import sqlite3
import pandas as pd
from xlsxwriter import Workbook

# Connect to SQLite database
conn = sqlite3.connect('sberindex.db')

# List of table names to convert
tables = [
    'primary_deals',
    'secondary_deals',
    'primary_offers',
    'secondary_offers',
    'primary_volume',
    'secondary_volume',
    'secondary_exposure'
]

# Create an Excel writer object
with pd.ExcelWriter('reshaped_sberindex_data.xlsx', engine='xlsxwriter') as writer:
    # Loop through each table
    for table in tables:
        # Load the table into a Pandas DataFrame
        query = f"SELECT * from {table}"
        df = pd.read_sql_query(query, conn)

        # Pivot the DataFrame
        pivot_df = df.pivot(index='date', columns='region', values='value')

        # Write DataFrame to a separate sheet in the Excel file
        pivot_df.to_excel(writer, sheet_name=table)

# Close the SQLite database connection
conn.close()
