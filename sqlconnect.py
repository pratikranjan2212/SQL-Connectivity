# import mysql.connector as sql
# db=sql.connect(host='localhost',user='root',passwd='root',auth_plugin='mysql_native_password')
# if db.is_connected():
#     print("Successfully connected")
# else:
#     print("Not connected")

# Mycur=db.cursor()
# Mycur.execute("Create database Employee")
# print("Successfully created database")
# Mycur.close()
# db.close()

import mysql.connector as sql
db=sql.connect(host='localhost',user='root',passwd='root',database='Employee',auth_plugin='mysql_native_password')
Mycur=db.cursor()
Mycur.execute("Create table emp2(name varchar(9),sal integer,desig varchar(8))")
Mycur.execute("show tables")
for x in Mycur:
    print(x)

