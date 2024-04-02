import psycopg2

    # Veritabanı bağlantısı kur
host = "midterm-db.postgres.database.azure.com"
dbname = "postgres"
user = "dengin"
password = "Abcd1234"
sslmode = "require"

# Construct connection string

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4} ".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

cursor.execute("SELECT * FROM customer;")
rows = cursor.fetchall()

# # Print all rows

for row in rows:
    print("Data row = (%s, %s)" %(str(row[0]), str(row[1])))

conn.commit()
cursor.close()
conn.close()


def main():
    print("Hello world")

if __name__ == "__main__":
    main()