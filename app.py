from flask import Flask, request, jsonify
from warehouse_optimizer import optimize_warehouse

app = Flask(__name__)

@app.route('/optimize-warehouse', methods=['POST'])
def optimize():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        result = optimize_warehouse(data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
