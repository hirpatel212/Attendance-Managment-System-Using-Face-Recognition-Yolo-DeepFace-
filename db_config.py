
# Database connection settings
DB_CONFIG = {
    'host': 'localhost',
    'username': 'root',
    'password': 'abcd1234',
    'database': 'face_recognizer_yolo' 
}

def get_connection():
    
    import mysql.connector
    return mysql.connector.connect(
        host=DB_CONFIG['host'],
        username=DB_CONFIG['username'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database']
    )
