from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("chat.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_message():
    data = request.get_json()
    username = data["username"]
    message = data["message"]

    conn = get_db()
    conn.execute(
        "INSERT INTO messages (sender, message) VALUES (?, ?)",
        (username, message)
    )
    conn.commit()
    conn.close()

    return jsonify({"status": "ok"})

@app.route("/messages")
def get_messages():
    conn = get_db()
    rows = conn.execute(
        "SELECT sender, message FROM messages ORDER BY id ASC"
    ).fetchall()
    conn.close()

    return jsonify([
        {"username": r["sender"], "message": r["message"]}
        for r in rows
    ])

if __name__ == "__main__":
    app.run()
