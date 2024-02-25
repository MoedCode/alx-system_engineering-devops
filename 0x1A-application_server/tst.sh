"
The error you encountered in running the addData.py script was related to the
absence of the mysqlclient library, which is a MySQL adapter for Python.
The solution involved installing the necessary dependencies
and the mysqlclient library using the following commands:
"

sudo apt-get install pkg-config libssl-dev
sudo pip3 install mysqlclient
"
These commands ensure that the required dependencies for building mysqlclient are installed,
 and then they install the Python MySQL adapter (mysqlclient).
 After running these commands, you were able to execute the addData.py script successfully.
 "