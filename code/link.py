import pyodbc

# Define your SQL Server connection parameters
server = 'PRANAV\SQLEXPRESS'
database = 'master'
# username = 'your_username'
# password = 'your_password'

# Create a connection to the SQL Server database
connection_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={database};'
# UID={username};PWD={password}
connection = pyodbc.connect(connection_string)

# Create a cursor to execute SQL queries
cursor = connection.cursor()

try:
    # Execute the SQL query to link the two tables and retrieve matching records
    sql_query = """
    SELECT l.BUSINESS_RO_ENTITY, l.NETWORK_ID
    FROM LINK AS l
    INNER JOIN RESP_ORG_ENTY AS r ON r.[Business RO Entity] = l.[BUSINESS_RO_ENTITY]
    """
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(f"BUSINESS_RO_ENTITY: {row.BUSINESS_RO_ENTITY}, NETWORK_ID: {row.NETWORK_ID}")


    sql_query1 = """
    SELECT l.BUSINESS_RO_ENTITY, l.NETWORK_ID
    FROM LINK AS l
    INNER JOIN RESP_ORG_UNIT AS r ON r.[BUSINESS_RO_ENTITY] = l.[BUSINESS_RO_ENTITY]
    """
    
    # Execute the query and fetch the results
    
    cursor.execute(sql_query1)
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(f"BUSINESS_RO_ENTITY: {row.BUSINESS_RO_ENTITY}, NETWORK_ID: {row.NETWORK_ID}")
    
        
except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the cursor and the database connection
    cursor.close()
    connection.close()
