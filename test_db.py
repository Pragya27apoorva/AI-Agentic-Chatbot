import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",    
        user="postgres",           
        password="Jan27@2005",  
        port="5432"
    )
    print("✅ Connection successful!")

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM agent_logs;")
    count = cur.fetchone()[0]
    print(f"📊 agent_logs table has {count} rows.")

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Error:", e)
