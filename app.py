#!flask/bin/python
from flask import Flask
from flask import abort
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "LETS DO THIS"

@app.route('/jobs/api/v1.0/likelihoods/<string:job_title>', methods=['GET'])
def get_likelihood(job_title):
    if len(job_title) == 0:
        abort(404)
    return jsonify({'likelihood': '12%'})

if __name__ == '__main__':
    app.run(debug=True)
