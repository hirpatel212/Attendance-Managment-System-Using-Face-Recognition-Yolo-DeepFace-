"""
Database Setup Script
Run this once to create the database and table
"""
import mysql.connector
from db_config import DB_CONFIG

def setup_database():
    print("=" * 60)
    print("Face Recognition System - Database Setup")
    print("=" * 60)
    
    # Connect to MySQL without specifying database
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG['host'],
            username=DB_CONFIG['username'],
            password=DB_CONFIG['password']
        )
        cursor = conn.cursor()
        print(f"\n✓ Connected to MySQL server")
        
        # Create database
        database_name = DB_CONFIG['database']
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"✓ Database '{database_name}' created/verified")
        
        # Use the database
        cursor.execute(f"USE {database_name}")
        
        # Create student table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS student (
            Dep VARCHAR(100),
            Subject VARCHAR(100),
            Year VARCHAR(100),
            Semester VARCHAR(100),
            Student_id INT PRIMARY KEY,
            Name VARCHAR(100),
            Division VARCHAR(50),
            Roll VARCHAR(50),
            Gender VARCHAR(20),
            DOB VARCHAR(50),
            Email VARCHAR(100),
            Phone VARCHAR(50),
            Address VARCHAR(200),
            Teacher VARCHAR(100),
            Photosample VARCHAR(10)
        )
        """
        cursor.execute(create_table_query)
        print(f"✓ Table 'student' created/verified")
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("\n" + "=" * 60)
        print("✓ Database setup completed successfully!")
        print("=" * 60)
        print(f"\nDatabase Name: {database_name}")
        print(f"Host: {DB_CONFIG['host']}")
        print(f"Username: {DB_CONFIG['username']}")
        print("\nYou can now run the application:")
        print("  python main.py")
        print("=" * 60)
        
    except mysql.connector.Error as err:
        print(f"\n✗ Error: {err}")
        print("\nPlease check:")
        print("1. MySQL server is running")
        print("2. Username and password in db_config.py are correct")
        print("3. User has permission to create databases")
        return False
    
    return True

if __name__ == "__main__":
    print("\nThis will create the database and table for the Face Recognition System")
    print(f"Database name: {DB_CONFIG['database']}")
    
    response = input("\nDo you want to continue? (y/n): ").strip().lower()
    
    if response == 'y':
        setup_database()
    else:
        print("\nSetup cancelled.")
