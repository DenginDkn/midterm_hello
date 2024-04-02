import psycopg2
# Update connection string information

host = "denginlogin.postgres.database.azure.com"
dbname = "denginpostgresql"
user = "dengin"
password = "Abcd1234"
sslmode = "require"

# Construct connection string

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4} ".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

# Fetch all rows from table

cursor.execute("SELECT * FROM customer;")
rows = cursor.fetchall()

# # Print all rows

for row in rows:
    print("Data row = (%s, %s)" %(str(row[0]), str(row[1])))

conn.commit()
cursor.close()
conn.close()
    
    
## INSERT
    
cursor.execute("INSERT INTO customer (customer_name, customer_gender) VALUES (%s, %s);", ("dengindkn", 'male'))
cursor.execute("INSERT INTO customer (customer_name, customer_gender) VALUES (%s, %s);", ("volkang", 'male'))
cursor.execute("INSERT INTO customer (customer_name, customer_gender) VALUES (%s, %s);", ("zeyneps", 'female'))
print("Inserted 3 rows of data")

conn.commit()
cursor.close()
conn.close()

## UPDATE

cursor.execute("UPDATE customer SET customer_name = %s WHERE customer_name = %s;", ("dengindd", "dengindkn"))
print("Updated 1 row of data")

conn.commit()
cursor.close()
conn.close()

## DELETE 

cursor.execute("DELETE FROM customer WHERE customer_name = %s;", ("dengindd",))
print("Deleted 1 row of data")

conn.commit()
cursor.close()
conn.close()