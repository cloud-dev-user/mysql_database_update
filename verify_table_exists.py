import os 
import mysql.connector

db_username = os.environ.get('mysql_user')
db_password = os.environ.get('mysql_pass')
database_name = os.environ.get('mysql_db')
db_host = os.environ.get('mysql_db_host')

# Set database configuration
db_config = {
    'host':  db_host,
    'user':  db_username,
    'password': db_password,
    'database': database_name
}

# Connect to MySQL database
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    print('Connected to MySQL database successfully')
    
    # Check if database exists
    cursor.execute('SHOW DATABASES')
    databases = [db[0] for db in cursor.fetchall()]
    if db_config['database'] in databases:
        print(f'Database "{db_config["database"]}" exists')
    else:
        print(f'Database "{db_config["database"]}" does not exist')
    
    # Check if table exists
    cursor.execute('SHOW TABLES')
    tables = [table[0] for table in cursor.fetchall()]
    if '<table_name>' in tables:
        print(f'Table "<table_name>" exists')
    else:
        print(f'Table "<table_name>" does not exist')
    
    cursor.close()
    conn.close()
except mysql.connector.Error as err:
    print(f'Error: {err}')
