import mysql.connector as sql
db=sql.connect(host='localhost',user='root',passwd='root',database='Employee',auth_plugin='mysql_native_password')
Mycur=db.cursor()

#insert multiple records at once
data="insert into emp2 (name,sal,desig)values(%s,%s,%s)"
em=[('Sudhir',4000,'mgr'),('Subham',6000,'admin'),('kanishk',7000,'mkt'),('sohan',9000,'md'),]
db.commit()
Mycur.executemany(data,em)
db.commit()

#insert multiple records as per user's choice
while True:
    r=input("Enter Employee Name:")
    n=int(input('Enter Salary:'))
    d=input('Enter Designation:')
    query="insert into emp2 values ('{}',{},'{}')".format(r,n,d)

    Mycur.execute(query)
    db.commit()
    print('Row inserted successfully')
    ch=input("Do you want to enter more records?(Y/N)")
    if ch=='n':
       break
    print("Row inserted successfully")

#fetching all records
Mycur.execute('select *from emp2')
myresult=Mycur.fetchall()
print('All records-')
for i in myresult:
    print(i)
print('Total no. of rows received=',Mycur.rowcount)

#fetching specific records
myresult=Mycur.fetchmany(4)
print('Multiple records-')
for i in myresult:
    print(i)
print('Total no. of rows received=',Mycur.rowcount)

#fetching single record
myresult=Mycur.fetchone()
print('Single record-')
print(myresult)
print('Total no. of rows received=',Mycur.rowcount)

#Updating records
nam=input('Enter name to be updated:')
sal=int(input('Enter salary to be set in the specified name:'))
Mycur.execute("update emp2 set sal={} where name='{}'".format(sal,nam))
db.commit()
print("Row updated successfully")

#Updating records
nam=input('Enter name to be updated:')
sal=int(input('Enter salary to be set in the specified name:'))
Mycur.execute("update emp2 set sal=%s where name='%s' and sal>4000"%(sal,nam))
db.commit()
print("Row updated successfully")

#Deleting records
d=input('Enter Desig for the record to be deleted:')
query="Delete from emp2 where desig='{}'".format(d)
Mycur.execute(query)
db.commit()
print("Row deleted successfully")