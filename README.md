# mysql_database_update

This is simple project containing Jenkinsfile and python script using whihc database can be created and updated. Make sure you install mysql connect for python 

### $ pip3 install mysql-connector-python

Also, make you have mysql database and user created.  you can refer following commands to verify or create the same 

 // Install MySQL client
 
     $ sudo apt-get update
     
     $ sudo apt-get install -y mysql-client
      
// Create database and user

      $ mysql -h <db_host> -u <db_user> -p<db_password> -e "CREATE DATABASE mydb;"
      
      $ mysql -h <db_host> -u <db_user> -p<db_password> -e "CREATE USER \'myuser\'@\'%\' IDENTIFIED BY \'mypassword\';"
      
      $ mysql -h <db_host> -u <db_user> -p<db_password> -e "GRANT ALL PRIVILEGES ON mydb.* TO \'myuser\'@\'%\';"
      
