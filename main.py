from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['POST'])
def test():
    return jsonify(
        resume=request.json['resume'],
        job_description=request.json['job_description']
        )

# run server
if __name__ == '__main__':
    app.run(host='localhost', debug=True)