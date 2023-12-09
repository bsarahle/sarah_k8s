
from flask import Flask, render_template, request, jsonify
import redis

app = Flask(__name__)
redis_db = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    key = request.form['key']
    value = request.form['value']
    if key and value:
        redis_db.set(key, value)
        return jsonify({'message': 'Logged in successfully'})            
    else:
        return jsonify({'error': 'Username or Password is incorrect'})

@app.route('/retrieve/<key>', methods=['GET'])
def retrieve_data(key):
    value = redis_db.get(key)
    if value:
        return jsonify({key: value.decode('utf-8')})
    else:
        return jsonify({'error': 'Key not found'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)