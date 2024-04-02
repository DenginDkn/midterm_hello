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

cursor.execute("INSERT INTO customer (customer_name, customer_gender) VALUES (%s, %s);", ("alimert", 'male'))
cursor.execute("INSERT INTO customer (customer_name, customer_gender) VALUES (%s, %s);", ("dendenn", 'male'))
cursor.execute("INSERT INTO customer (customer_name, customer_gender) VALUES (%s, %s);", ("elif", 'female'))
print("Inserted 3 rows of data")

conn.commit()
cursor.close()
conn.close()


def main():
    print("Hello world")

if __name__ == "__main__":
    main()