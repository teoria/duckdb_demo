import duckdb

def main(): 
    # Connect to an in-memory DuckDB database
    con = duckdb.connect(database=':memory:')

    # Create a sample table
    con.execute("CREATE TABLE items (id INTEGER, name STRING)")
    
    # Insert some sample data
    con.execute("INSERT INTO items VALUES (1, 'item1'), (2, 'item2'), (3, 'item3')")

    # Query the table
    result = con.execute("SELECT * FROM items")
    
    #Print the results
    for row in result.fetchall():
        print(row)
        
    #print(result.fetch_df())

if __name__ == "__main__":
    main()