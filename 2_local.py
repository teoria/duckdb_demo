import duckdb


def create_table():   
    with duckdb.connect(database='taxi.db') as con: 
        con.execute("CREATE OR REPLACE TABLE taxi_data as select * from 'taxi/*.parquet'")
      
def main():
    with duckdb.connect(database='taxi.db') as con:  
        # Query the table
        result = con.execute("SELECT count(*),avg(total_amount) FROM taxi_data").fetch_df()
        print(result)

if __name__ == "__main__":
    create_table()
    #main()