pipeline {
    agent any
    
    stages {
        stage('Verify if table exist else create the table in MYSQL') {
            steps {
                    sh """
                     mysql -h <db_host> -P 3306 -u <db_user> -p <db_pass> "USE <database_name>;"
                     if [ "$?" == "0" ]; then 
                                echo "database created" 
                     else 
                                 echo "Please verify if database exists" 
                     exit 1
                     fi 
                     """
                     error "Database is not created" 
                
            }
        }
        
        stage('Create  table and insert data') {
            steps {
                     sh """
                         ./verify_table_exists.py 
                        if [ "$?" == "0" ]; then 
                                echo "table is present and we can go to update table stage" 
                        else 
                               echo "table doesn't exists and we will create the table & inset sample data" 
                                ./mysql_create_table.py && mysql_insert_data.py 
                        fi
                      """
                }
            }
         stage('Update table') {
            steps {
                     sh """
                      ./mysql_update.py
                      """
                }
            }
        }
        }
    }
}
