from flask import Flask, jsonify
import psycopg2

# Initialize Flask app
app = Flask(__name__)

# --- Database connection function ---
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="postgres",   
        user="postgres",       
        password="Jan27@2005",  
        port="5432"
    )

# --- Home Route ---
@app.route('/')
def home():
    return "✅ Flask app is running successfully!"

# --- Metrics Route ---
@app.route('/metrics')
def get_metrics():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM agent_logs ORDER BY created_at DESC LIMIT 20;")
        data = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True)
