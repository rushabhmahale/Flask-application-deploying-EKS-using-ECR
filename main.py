from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'This Flask application running on EKS <h1>Hello Running From K8S</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
