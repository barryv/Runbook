import pyodbc

# Define the connection parameters
server = 'AH-1293878-001.sdi.bankofamerica.com'  # e.g., 'localhost' or '192.168.1.1'
database = 'Warehouse'  # e.g., 'TestDB'
username = 'RTD_READ'  # e.g., 'sa'
password = 'whgwimd70581'  # e.g., 'your_password'

# Create the connection string
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Establish the connection
try:
    connection = pyodbc.connect(connection_string)
    print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")

# Use the connection (e.g., execute a query)
try:
    cursor = connection.cursor()
    cursor.execute("SELECT @@APSREMON_JIRA;")
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
except Exception as e:
    print(f"Error: {e}")
finally:
    # Close the connection
    connection.close()
    print("Connection closed.")

