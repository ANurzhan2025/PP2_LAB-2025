import psycopg2
import csv
from tabulate import tabulate

conn = psycopg2.connect(
    host="localhost",
    dbname="lab10",
    user="postgres",
    password="1234",
    port=5432
)
cur = conn.cursor()

def insert_data():
    filepath = input("Enter a file path with proper extension: ")
    try:
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                print(f"Processing row: {row}")  # Печатаем строку для отладки
                if len(row) == 3:
                    name, surname, phone = row
                    cur.execute("SELECT * FROM phonebook WHERE name = %s AND surname = %s", (name, surname))
                    existing_user = cur.fetchone()
                    if existing_user:
                        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s AND surname = %s", (phone, name, surname))
                        print(f"Updated phone number for {name} {surname}.")
                    else:
                        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
                        print(f"Inserted new user: {name} {surname}.")
                else:
                    print(f"Skipping invalid row: {row}. Expected 3 columns (name, surname, phone).")
        conn.commit()
        print("Data successfully inserted or updated.")
    except Exception as e:
        print("Error while inserting data:", e)

def query_data():
    pattern = input("Enter pattern to search (name, surname or phone): ")
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR surname ILIKE %s OR phone ILIKE %s", 
                (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt="pretty"))

def delete_data():
    info = input("Enter name or phone to delete: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (info, info))
    conn.commit()
    print("Data deleted.")

def show_data():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt="pretty"))

def menu():
    print("""
    List of the commands:
    1. Type "i" or "I" in order to INSERT data to the table.
    2. Type "u" or "U" in order to UPDATE data in the table.
    3. Type "q" or "Q" in order to make specific QUERY in the table.
    4. Type "d" or "D" in order to DELETE data from the table.
    5. Type "s" or "S" in order to see the values in the table.
    6. Type "f" or "F" in order to close the program.
    """)

while True:
    menu()
    command = input("Enter command: ")
    if command.lower() == "i":
        insert_data()
    elif command.lower() == "q":
        query_data()
    elif command.lower() == "d":
        delete_data()
    elif command.lower() == "s":
        show_data()
    elif command.lower() == "f":
        break
    else:
        print("Wrong command!")

cur.close()
conn.close()