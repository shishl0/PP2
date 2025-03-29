import psycopg2
import sys

# Every function from above exists as a procedure in a db "phonebookdb"

def create_connection():
    """ Establish and return a connection to the PostgreSQL database. """
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="phonebookdb",
            user="zhan",
            password=""
        )
        return conn
    except Exception as e:
        print("Error connecting to the database:", e)
        sys.exit(1)

def create_table(conn):
    """ Ensure the phonebook table exists. """
    cur = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone VARCHAR(50) NOT NULL
    );
    """
    cur.execute(create_table_query)
    conn.commit()
    cur.close()

# 1️ Function: Get records by pattern (name, phone)
def search_by_pattern(conn):
    """ Search records by pattern (name/phone). """
    pattern = input("Enter pattern to search: ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_records(%s);", (pattern,)) # procedure "search_records(%s)"
    rows = cur.fetchall()
    
    if rows:
        print("\nMatching Records:")
        for row in rows:
            print(row)
    else:
        print("\nNo records found.")
    
    cur.close()

# 2️ Procedure: Insert or Update a User
def insert_or_update_user(conn):
    """ Insert or update a user in the phonebook. """
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone)) # procedure "insert_or_update_user(%s, %s)"
    conn.commit()
    cur.close()
    print(f"User {name} inserted/updated successfully.")

# 3️ Procedure: Bulk Insert Users with Phone Validation
def insert_bulk_users(conn):
    """ Insert multiple users at once. """
    user_list = []
    
    while True:
        name = input("Enter name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        phone = input("Enter phone: ")
        user_list.append([name, phone])
    
    if user_list:
        cur = conn.cursor()
        cur.execute("CALL insert_bulk_users(%s);", (user_list,)) # procedure "insert_bulk_users(%s)"
        conn.commit()
        cur.close()
        print("Bulk user insertion completed.")

# 4️ Function: Paginated Querying
def get_paginated_results(conn):
    """ Retrieve paginated records. """
    limit = int(input("Enter number of records per page: "))
    offset = int(input("Enter offset (starting position): "))
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_paginated_data(%s, %s);", (limit, offset)) # procedure "get_paginated_data(%s, %s)"
    rows = cur.fetchall()
    
    if rows:
        print("\nPaginated Results:")
        for row in rows:
            print(row)
    else:
        print("\nNo more records to display.")
    
    cur.close()

# 5️ Procedure: Delete User by Name or Phone
def delete_user(conn):
    """ Delete a user by name or phone. """
    identifier = input("Enter name or phone to delete: ")
    cur = conn.cursor()
    cur.execute("CALL delete_user(%s);", (identifier,)) # procedure "delete_user(%s)"
    conn.commit()
    cur.close()
    print(f"User '{identifier}' deleted successfully.")

def main():
    """ Main menu for the phonebook application. """
    conn = create_connection()
    create_table(conn)
    
    while True:
        print("\nPhoneBook Menu:")
        print("1. Search records by pattern")
        print("2. Insert or update user")
        print("3. Insert multiple users")
        print("4. Get paginated results")
        print("5. Delete user")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            search_by_pattern(conn)
        elif choice == '2':
            insert_or_update_user(conn)
        elif choice == '3':
            insert_bulk_users(conn)
        elif choice == '4':
            get_paginated_results(conn)
        elif choice == '5':
            delete_user(conn)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

    conn.close()

if __name__ == '__main__':
    main()