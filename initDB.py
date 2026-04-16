import mysql.connector

# DB Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yourpassword",
    database="AgroLoan",
    charset='utf8mb4',
    collation='utf8mb4_general_ci'  # This avoids MariaDB conflict
)

cursor = conn.cursor()

# SQL Query
create_table_query = """
CREATE TABLE IF NOT EXISTS farmers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    mobile VARCHAR(15) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    location VARCHAR(100),
    land_area DECIMAL(10,2),
    crop VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# Execute and close
cursor.execute(create_table_query)
conn.commit()
cursor.close()
conn.close()

print("Table 'farmers' created successfully.")
