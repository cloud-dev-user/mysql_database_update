import os 
import mysql.connector

username = os.environ.get('mysql_user')
password = os.environ.get('mysql_pass')
databse_name = os.environ.get('mysql_db')

# Establish database connection
cnx = mysql.connector.connect(user='username', password='password', host='localhost', database='database_name')

# Define the SQL script
sql_script = """
INSERT INTO customers (first_name, last_name, email, address, city, state, zip_code) VALUES
('John', 'Doe', 'john.doe@example.com', '456 Elm St', 'Springfield', 'IL', '12345'),
('Jane', 'Smith', 'jane.smith@example.com', '789 Oak Ave', 'Chicago', 'IL', '67890'),
('Bob', 'Johnson', 'bob.johnson@example.com', '321 Pine St', 'St. Louis', 'MO', '54321');
"""

# Execute the SQL script
cursor = cnx.cursor()
cursor.execute(sql_script)

# Commit the changes
cnx.commit()

# Close database connection
cursor.close()
cnx.close()
