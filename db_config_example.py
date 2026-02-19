"""
Database Configuration Template
================================

IMPORTANT: 
1. Copy this file to 'db_config.py'
2. Update the values with your MySQL credentials
3. Never commit db_config.py to GitHub (it's in .gitignore)

Usage:
------
cp db_config_example.py db_config.py
# Then edit db_config.py with your credentials
"""

# Database connection settings
DB_CONFIG = {
    'host': 'localhost',              # MySQL host (usually localhost)
    'username': 'root',               # Your MySQL username
    'password': 'your_password_here', # Your MySQL password (CHANGE THIS!)
    'database': 'face_recognizer_yolo' # Database name
}

def get_connection():
    """
    Returns a MySQL connection using the configured settings
    
    Returns:
        mysql.connector.connection: Database connection object
    
    Raises:
        mysql.connector.Error: If connection fails
    """
    import mysql.connector
    return mysql.connector.connect(
        host=DB_CONFIG['host'],
        username=DB_CONFIG['username'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database']
    )


# Example usage:
# from db_config import get_connection
# conn = get_connection()
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM student")
# results = cursor.fetchall()
# conn.close()
