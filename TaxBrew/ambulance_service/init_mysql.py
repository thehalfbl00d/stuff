import pymysql
from config.config import Config

def create_database():
    # Connect to MySQL server without selecting a database
    connection = pymysql.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD
    )
    
    try:
        with connection.cursor() as cursor:
            # Create database if it doesn't exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.MYSQL_DB}")
            print(f"Database '{Config.MYSQL_DB}' created successfully!")
            
    finally:
        connection.close()

if __name__ == "__main__":
    create_database()
