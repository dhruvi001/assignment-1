from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(database="users_db", user="user", password="password", host="db", port="5432")

@app.route('/api/data', methods=['POST'])
def store_data():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (data['name'], data['email']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Data stored successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
