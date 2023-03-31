import os
import mysql.connector

username = os.environ.get('mysql_user')
password = os.environ.get('mysql_pass')
databse_name = os.environ.get('mysql_db')

# Establish database connection
cnx = mysql.connector.connect(user='username', password='password', host='localhost', database='database_name')

# Define the SQL script
sql_script = """
CREATE TABLE customers (
  customer_id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  address VARCHAR(100) NOT NULL,
  city VARCHAR(50) NOT NULL,
  state VARCHAR(50) NOT NULL,
  zip_code VARCHAR(10) NOT NULL,
  PRIMARY KEY (customer_id)
);
"""

# Execute the SQL script
cursor = cnx.cursor()
cursor.execute(sql_script)

# Commit the changes
cnx.commit()

# Close database connection
cursor.close()
cnx.close()
