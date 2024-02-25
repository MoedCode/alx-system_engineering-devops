-- Check if hbnb_dev_db exists
SELECT IF(EXISTS (SELECT 1 FROM information_schema.schemata WHERE schema_name = 'hbnb_dev_db'), 'Database exists', 'Database does not exist') AS hbnb_dev_db_status;

-- Check if hbnb_test_db exists
SELECT IF(EXISTS (SELECT 1 FROM information_schema.schemata WHERE schema_name = 'hbnb_test_db'), 'Database exists', 'Database does not exist') AS hbnb_test_db_status;

-- Check if hbnb_dev user exists
SELECT IF(EXISTS (SELECT 1 FROM mysql.user WHERE user = 'hbnb_dev' AND host = 'localhost'), 'User exists', 'User does not exist') AS hbnb_dev_user_status;

-- Check if hbnb_test user exists
SELECT IF(EXISTS (SELECT 1 FROM mysql.user WHERE user = 'hbnb_test' AND host = 'localhost'), 'User exists', 'User does not exist') AS hbnb_test_user_status;

-- Create hbnb_dev_db database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create hbnb_test_db database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user hbnb_dev if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- Create user hbnb_test if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
