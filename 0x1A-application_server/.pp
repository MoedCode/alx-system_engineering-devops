{
erorr_prompt => ERROR 2002 (HY000): Cant connect to local MySQL server through socket /var/run/mysqld/mysqld.sock (2),
Reasone =>  i didnt then  mysql_server installed "inux ubntu 20.04 remote container ubuntu@449040-web-01 "
command_used
# 1- install mysql_server
Install=> sudo apt install mysql-server
 &&
# 2- restart or start mysql
start=>sudo service mysql start
||
restart=>sudo service mysql restart
}