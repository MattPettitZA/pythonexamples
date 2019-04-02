import sqlite3

conn = sqlite3.connect('mydb.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE test
#       (ID,name,mail)''')


c.execute("INSERT INTO test VALUES ('PET01','Matt Pettit','pettit.matt@gmail.com')")
for row in c.execute('SELECT * FROM test  ORDER BY ID'):
    print row
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
