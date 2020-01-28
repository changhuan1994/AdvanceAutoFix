from flask import (Flask, request, abort, jsonify)

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({
        'status': 'OK',
        'message': 'Hello World!',
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

