import mysql.connector as sql
conn = sql.connect(host = 'localhost', user = 'root', passwd = 'tiger', database='hotel')
c1 = conn.cursor()
c1.execute('create table laundryview(sno integer not null, itemname varchar(10), rate integer);')
c1.execute('insert into laundryview values(1,"pant", 10);')
c1.execute('insert into laundryview values(2,"shirt", 10);')
c1.execute('insert into laundryview values(3,"suit", 10);')
c1.execute('insert into laundryview values(4,"sari", 10);')
           
conn.commit()
print('table created successfully')
