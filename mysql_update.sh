import mysql.connector

# Establish database connection
cnx = mysql.connector.connect(user='username', password='password', host='localhost', database='database_name')

# Create a savepoint
cursor = cnx.cursor()
cursor.execute("SAVEPOINT my_savepoint")

try:
    # Execute some SQL statements
    cursor.execute("UPDATE customers SET address = '123 Main St' WHERE customer_id = 1")
    cursor.execute("DELETE FROM orders WHERE customer_id = 1")
    
    # Commit the changes
    cnx.commit()
    print("Changes committed successfully!")
except:
    # Rollback to the savepoint if an error occurs
    cursor.execute("ROLLBACK TO my_savepoint")
    print("Changes rolled back!")
    
    # Discard the savepoint
    cursor.execute("RELEASE my_savepoint")

# Close database connection
cursor.close()
cnx.close()
