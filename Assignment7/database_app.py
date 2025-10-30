import psycopg2

# Step 1: Connect to PostgreSQL database
try:
    conn = psycopg2.connect(
        host="localhost",      # Database host
        database="testdb",     # Database name
        user="postgres",       # Default username
        password="yourpassword" # Change to your PostgreSQL password
    )
    print("✅ Database connection successful!")

except Exception as e:
    print("❌ Error connecting to database:", e)
    exit()

# Step 2: Create a cursor object to run SQL commands
cur = conn.cursor()

# Step 3: Create a simple table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    course VARCHAR(50)
)
""")
conn.commit()
print("📘 Table created successfully!")

# Step 4: Insert data
cur.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)", ("Aizen", 20, "Data Science"))
conn.commit()
print("🧩 Data inserted successfully!")

# Step 5: Fetch data
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
print("\n🎯 All Students:")
for row in rows:
    print(row)

# Step 6: Close the connection
cur.close()
conn.close()
print("\n🔒 Connection closed.")
