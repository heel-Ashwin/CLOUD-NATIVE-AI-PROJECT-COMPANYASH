import mysql.connector
import bcrypt

def init_database():
    try:
        conn = mysql.connector.connect(user='root', password='1234', host='localhost')
        cursor = conn.cursor()
        

        cursor.execute("CREATE DATABASE IF NOT EXISTS CompanyASH")
        conn.database = 'CompanyASH'
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            username VARCHAR(50) UNIQUE,
                            password VARCHAR(100),
                            role ENUM('supervisor', 'admin', 'user'),
                            email VARCHAR(100),
                            is_verified BOOLEAN DEFAULT FALSE
                         )''')
                         
        cursor.execute('''CREATE TABLE IF NOT EXISTS employee_data (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(50),
                            dob DATE,
                            department VARCHAR(50),
                            location VARCHAR(50),
                            role VARCHAR(10)
                         )''')

        cursor.execute("SELECT * FROM users WHERE role = 'supervisor'")
        if not cursor.fetchone():
            password = bcrypt.hashpw("supervisorpassword".encode(), bcrypt.gensalt()).decode()
            cursor.execute("INSERT INTO users (username, password, role, email, is_verified) VALUES (%s, %s, 'supervisor', %s, %s)",
                           ('developer', password, 'ar1021@srmist.edu.in', True))
        
        conn.commit()
        print("Database and tables created successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    init_database()
