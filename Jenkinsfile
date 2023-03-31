pipeline {
    agent any
    
    stages {
        stage('Verify if table exist else create the table in MYSQL') {
            steps {
              
              
                // Install MySQL client
                sh 'sudo apt-get update'
                sh 'sudo apt-get install -y mysql-client'
                
                // Create database and user
                sh 'mysql -h <db_host> -u <db_user> -p<db_password> -e "CREATE DATABASE mydb;"'
                sh 'mysql -h <db_host> -u <db_user> -p<db_password> -e "CREATE USER \'myuser\'@\'%\' IDENTIFIED BY \'mypassword\';"'
                sh 'mysql -h <db_host> -u <db_user> -p<db_password> -e "GRANT ALL PRIVILEGES ON mydb.* TO \'myuser\'@\'%\';"'
            }
        }
        
        stage('Update database') {
            steps {
                // Run SQL script to create new table
                withCredentials([string(credentialsId: 'mysql_password', variable: 'MYSQL_PASSWORD')]) {
                    sh 'mysql -h <db_host> -u myuser -p"$MYSQL_PASSWORD" mydb < create_table.sql'
                }
                
                // Insert sample data into new table
                withCredentials([string(credentialsId: 'mysql_password', variable: 'MYSQL_PASSWORD')]) {
                    sh 'mysql -h <db_host> -u myuser -p"$MYSQL_PASSWORD" mydb < insert_data.sql'
                }
            }
        }
        
        stage('Rollback changes') {
            steps {
                // Rollback changes using SQL script
                withCredentials([string(credentialsId: 'mysql_password', variable: 'MYSQL_PASSWORD')]) {
                    sh 'mysql -h <db_host> -u myuser -p"$MYSQL_PASSWORD" mydb < rollback.sql'
                }
            }
        }
    }
}
