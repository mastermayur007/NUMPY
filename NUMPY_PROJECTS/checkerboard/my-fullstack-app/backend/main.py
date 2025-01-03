import numpy as np
from flask import Flask, request, jsonify

def checkbord(n):
    final = []
    for i in range(n):
        final.append(list(np.tile([0, 1], n // 2)))
        if n % 2 == 0:
            final[i] = final[i][:n]  # Ensure the row is of length n
        else:
            final[i] = final[i][:n] + [1]  # Add an extra 1 for odd n
    return np.array(final).tolist()  # Convert to list for JSON serialization

app = Flask(__name__)

@app.route('/checkbord', methods=['POST'])
def generate_checkbord():
    data = request.json
    n = data.get('size', 0)
    if n <= 0:
        return jsonify({"error": "Size must be a positive integer."}), 400
    checkerboard = checkbord(n)
    return jsonify(checkerboard)

if __name__ == '__main__':
    app.run(debug=True)