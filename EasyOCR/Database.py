import mysql.connector

def display_table_contents():
    # Connect to the database
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='spring',
        port='3306',
        database='test'
    )

    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    # Query to select specific columns from the table
    column_names = ['alcohol_content', 'bottle_information', 'brand_name', 'grape_variety',
                    'vintage', 'wine_name', 'region_of_production']

    query = "SELECT " + ", ".join(column_names) + " FROM wine_label"

    # Execute the query
    mycursor.execute(query)

    # Fetch all rows
    all_records = mycursor.fetchall()

    # Print the column headers
    print("Column Names:", column_names)

    # Print the table contents
    for record in all_records:
        print(record)

    # Close the cursor and database connection
    mycursor.close()
    mydb.close()

if __name__ == "__main__":
    display_table_contents()
