#!/bin/bash

echo "1. Checking Python3..."
if command -v python3 &>/dev/null; then
    echo "   Python3 is already installed."
else
    echo "   Installing 📦 Python3..."
    sudo apt-get update
    sudo apt-get install -y python3
fi

echo "2. Checking Pip3..."
if command -v pip3 &>/dev/null; then
    echo "   Pip3 is already installed."
else
    echo "   Installing 📦 Pip3..."
    sudo apt-get install -y python3-pip
fi

echo "3. Checking SQLAlchemy..."
if python3 -c "import sqlalchemy" &>/dev/null; then
    echo "   SQLAlchemy is already installed."
else
    echo "   Installing 📦 SQLAlchemy..."
    pip3 install sqlalchemy
fi

echo "4. Checking MySQLdb..."
if python3 -c "import MySQLdb" &>/dev/null; then
    echo "   MySQLdb is already installed."
else
    echo "   Installing 📦 MySQLdb..."
    sudo apt-get install -y libmysqlclient-dev
    pip3 install mysqlclient
fi

echo "5. Checking Flask..."
if python3 -c "import flask" &>/dev/null; then
    echo "   Flask is already installed."
else
    echo "   Installing 📦 Flask..."
    pip3 install flask
fi

echo "6. Checking Gunicorn..."
if command -v gunicorn &>/dev/null; then
    echo "   Gunicorn is already installed."
else
    echo "   Installing 📦 Gunicorn..."
    pip3 install gunicorn
fi

echo "All packages are installed successfully!"
: '
so  provide a bash script that
1- install python3
2- install pyhton3 pip3 if pip3
3- install mysql alchemy   and all dependencies
like we do for mysql clint

 4- MySQLdb and also with all dependencies
5- install flask with all dependencies
6- install gunicorn with all dependencies
on each step from 1 to 6 script should check that each  package exists  first
note that all package will be installed for python3
and if it exists print a  appropriate message
and if it not  exists  and print a  appropriate message that tells
that the package will be installed like
__<step number >installing 📦   <package name >
'