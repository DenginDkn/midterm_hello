import psycopg2
import getpass

def connect_to_database():
    # Veritabanı bağlantısı kur
    host = "denginlogin.postgres.database.azure.com"
    dbname = "denginpostgresql"
    user = "dengin"
    password = "Abcd1234"
    sslmode = "require"

# Construct connection string

    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4} ".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    print("Connection established")
    return conn

def authenticate_user(username, password):
    # Kullanıcı Doğrula
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM customer WHERE customer_id = %s AND password = %s;", (username, password))
    count_row = cursor.fetchone()
    conn.close()

    # If count_row is None or count_row[0] is 0, authentication failed
    if count_row is not None:
        count = count_row[0]
        return count == 1
    else:
        return False


def main():
    username = input("Enter Customer id: ")
    password2 = getpass.getpass("Enter Password: ")

    if authenticate_user(username, password2):
        print("Login Succesfully.")
    else:
        print("Wrong ID or Password.")

if __name__ == "__main__":
    main()
    
