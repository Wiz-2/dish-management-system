from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import sqlite3

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

def get_db_connection():
    conn = sqlite3.connect('dishes.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/dishes', methods=['GET'])
def get_dishes():
    conn = get_db_connection()
    dishes = conn.execute('SELECT * FROM dishes').fetchall()
    conn.close()
    return jsonify([dict(dish) for dish in dishes])

@app.route('/toggle-publish/<int:id>', methods=['POST'])
def toggle_publish(id):
    conn = get_db_connection()
    dish = conn.execute('SELECT isPublished FROM dishes WHERE dishId = ?', (id,)).fetchone()
    if dish is None:
        return jsonify({'error': 'Dish not found'}), 404

    new_status = not dish['isPublished']
    conn.execute('UPDATE dishes SET isPublished = ? WHERE dishId = ?', (new_status, id))
    conn.commit()
    conn.close()
    
    socketio.emit('update', {'id': id, 'isPublished': new_status})
    
    return jsonify({'message': 'success'})

if __name__ == '__main__':
    socketio.run(app, debug=True)
