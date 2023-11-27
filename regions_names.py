import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('/home/kaarlahti/PycharmProjects/sberindex/sberindex.db')

# List of your table names
tables = ['primary_deals',
          'primary_offers',
          'primary_volume',
          'secondary_deals',
          'secondary_offers',
          'secondary_volume',
          'secondary_exposure']

unique_regions = set()

for table in tables:
    try:
        cursor = conn.execute(f'SELECT DISTINCT region FROM {table}')
        regions = cursor.fetchall()
        unique_regions.update([r[0] for r in regions])
    except Exception as e:
        print(f"An error occurred while querying {table}: {e}")

# Close the database connection
conn.close()

# Now, unique_regions contains all unique region names from all tables
print(unique_regions)
