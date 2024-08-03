import pandas as pd
import pyodbc

# Define the database connection parameters
server = 'PRANAV\SQLEXPRESS'
database = 'master'
driver = 'SQL SERVER'

# Establish a database connection
conn = pyodbc.connect(f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};')

# Define the path to your CSV file
csv_file = 'C:/VIT/carrier.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

# Iterate through the rows of the DataFrame and update the SQL Server table
cursor = conn.cursor()

for index, row in df.iterrows():
    carrier_code = row['Carrier  Code']
    business_ro_entity = row['Business RO Entity']
    network_id = row['Network ID']

    
    # Update the SQL Server table where EMP_ID matches the Carrier Code
    update_query = f"""
    UPDATE RESP_ORG_UNIT
    SET [BUSINESS_RO_ENTITY] = ?,
        [NETWORK_ID] = ?
    WHERE EMP_ID = ?
    """
        
    cursor.execute(update_query, (business_ro_entity, network_id, carrier_code))

# Commit the changes
conn.commit()

# Delete rows with NULL values in BUSINESS_RO_ENTITY and NETWORK_ID
delete_query = """
DELETE FROM RESP_ORG_UNIT
WHERE [BUSINESS_RO_ENTITY] IS NULL AND [NETWORK_ID] IS NULL OR LEN(ISNULL([BUSINESS_RO_ENTITY], '')) <> 5;
"""

# Execute the DELETE statement
cursor.execute(delete_query)

# Commit the changes
conn.commit()

# Close the database connection
conn.close()

print("Update completed successfully.")
